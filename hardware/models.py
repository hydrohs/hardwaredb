from django.db import models
from polymorphic.models import PolymorphicModel
import choices.models as Choices
import os.path

def HumanReadable(calc, value, ram_type):
    # Converts db values into more friendly human readable numbers for display
    def Size():
        if value >= 1048576: # If size is over this value we're dealing with terabytes
            size = value / 1048576
            return '{}{}'.format(str(int(size) if float(size).is_integer() else size), 'TB')
        elif value >= 1024: # Over this value is gigabytes
            size = value / 1024
            return '{}{}'.format(str(int(size) if float(size).is_integer() else size), 'GB')
        else: # Else just add MB to stored database value
            return '{}{}'.format(str(value), 'MB')
    
    def CpuFreq():
        if value >= 1000: # Simply convert large MHz into GHz
            return '{}{}'.format(str(value / 1000), 'GHz')
        else:
            return '{}{}'.format(value, 'MHz')
    
    def RamSpeed(): # Add suffix based on RAM type
        if ram_type == 'FPM' or ram_type =='EDO':
            return '{}{}'.format(str(int(value)), 'ns')
        else:
            return '{}{}'.format(str(int(value)), 'MHz')

    if calc == 'cpu':
        return CpuFreq()
    elif calc == 'size':
        return Size()
    elif calc == 'ram':
        return RamSpeed()
    else:
        return 'None'
    
def get_upload_path(instance, filename):
    base = instance.part.upload_base
    brand = instance.part.brand
    model = instance.part.model.replace('/', '') if instance.part.model else instance.part.model
    name = instance.part.name.replace('/', '') if instance.part.name else instance.part.name
    pk = instance.part.pk
    extension = os.path.splitext(filename)[1]
    if 'custom' in base:
        path = f'{base}/{name}/{instance.name}{extension}'
    elif ('micros' in base) or ('proprietary' in base):
        path = f'{base}/{brand}/{name}/{instance.name}{extension}'
    else:
        path = f'{base}/{brand}_{model}_{pk}/{instance.name}{extension}'

    return path

class Hardware(PolymorphicModel):
    brand = models.CharField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path)
    part = models.ForeignKey(Hardware, related_name='images', on_delete=models.CASCADE)

class System(Hardware):
    os = models.CharField(max_length=64, verbose_name='OS')
    upload_base = 'systems/custom'

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return "/systems/%i" % self.id
    
    def get_ram(self):
        # Loops through all RAM fields in order to add up total
        # then adds on RAM type/speed (even though this could technically be different, in my use it wont come up)
        # This function is used on system detail page to show total ram, rather than potentially many different ram
        # sticks (all likely to be the same) in a list
        ram = 0
        for i in self.ram.all():
            ram += i.size
        if ram:
            return '{} {} {}'.format(
                HumanReadable('size', ram, ''),
                HumanReadable('ram', self.ram.first().speed, self.ram.first().get_type_display()),
                self.ram.first().get_type_display()
                )
        else:
            return 0

class CPU(Hardware):
    speed = models.IntegerField()
    socket = models.CharField(max_length=200)
    cores = models.IntegerField()
    hyperthreading = models.BooleanField()
    cpu_world = models.TextField(null=True, blank=True)
    installed_in = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True, related_name='cpus')

    upload_base = 'cpus'

    def get_absolute_url(self):
        return "/cpus/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.name)

    def get_speed_display(self):
        return HumanReadable('cpu', self.speed, '')

    class Meta:
        verbose_name = 'CPU'
        verbose_name_plural = 'CPUs'

class RAM(models.Model):
    type = models.ForeignKey(Choices.RAMType, on_delete=models.SET_NULL, null=True)
    interface = models.ForeignKey(Choices.RAMInterface, on_delete=models.SET_NULL, null=True)
    size = models.IntegerField(verbose_name='Size (MB)')
    speed = models.IntegerField(verbose_name='Speed (ns or MHz)')
    ecc = models.BooleanField(verbose_name='ECC')
    installed_in = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram')

    def get_absolute_url(self):
        return "/ram/%i" % self.id

    def __str__(self):
        if self.ecc:
            is_ecc = 'ECC'
        else:
            is_ecc = ''

        return f'{HumanReadable("size", self.size, "")} {HumanReadable("ram", self.speed, self.type.name)} {self.type.name} {is_ecc} {self.interface.name}'

    class Meta:
        verbose_name = 'RAM'
        verbose_name_plural = 'RAM'

class GPU(Hardware):
    gpu_brand = models.CharField(max_length=32, verbose_name='GPU')
    interface = models.ForeignKey(Choices.Slot, on_delete=models.SET_NULL, null=True)
    mda = models.IntegerField(default=0, verbose_name='MDA Ports')
    cga = models.IntegerField(default=0, verbose_name='CGA Ports')
    composite = models.IntegerField(default=0, verbose_name = 'Composite Ports')
    vga = models.IntegerField(default=0, verbose_name='VGA Ports')
    svideo = models.IntegerField(default=0, verbose_name = 'S-Video Ports')
    component = models.IntegerField(default=0, verbose_name = 'Component Ports')
    dvi = models.IntegerField(default=0, verbose_name='DVI Ports')
    hdmi = models.IntegerField(default=0, verbose_name='HDMI Ports')
    minihdmi = models.IntegerField(default=0, verbose_name='Mini HDMI Ports')
    microhdmi = models.IntegerField(default=0, verbose_name='Micro HDMI Ports')
    dp = models.IntegerField(default=0, verbose_name='Displayport Ports')
    minidp = models.IntegerField(default=0, verbose_name='Mini DisplayPort Ports')
    other = models.IntegerField(default=0, verbose_name='Other Ports (Use notes)')
    installed_in = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True, related_name='gpus')

    upload_base = 'gpus'

    def get_absolute_url(self):
        return "/gpus/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.name)

    class Meta:
        verbose_name = 'GPU'
        verbose_name_plural = 'GPUs'

class SoundCard(Hardware):
    sb = models.CharField(max_length=200, verbose_name='SB Compatibility')
    interface = models.ForeignKey(Choices.Slot, on_delete=models.SET_NULL, null=True)
    installed_in = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True, related_name='soundcards')

    upload_base = 'sound_cards'

    def get_absolute_url(self):
        return "/sound_cards/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.name)

class ExpansionCard(Hardware):
    interface = models.ForeignKey(Choices.Slot, on_delete=models.SET_NULL, null=True)
    io_panel = models.CharField(max_length=255, null=True, blank=True, verbose_name='IO Panel (comma separated)')
    installed_in = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True, related_name='expansioncards')

    upload_base = 'expansion_cards'

    def get_absolute_url(self):
        return "/expansion_cards/%i" % self.id

    def __str__(self):
        if self.name is None:
            return f'{self.brand} {self.model}'
        else:
            return f'{self.name}'
    
class NIC(Hardware):   
    wireless = models.BooleanField()
    speed = models.ForeignKey(Choices.NetSpeed, on_delete=models.SET_NULL, null=True)
    interface = models.ForeignKey(Choices.Slot, on_delete=models.SET_NULL, null=True)
    aui = models.IntegerField(default=0, verbose_name='AUI Ports')
    bnc = models.IntegerField(default=0, verbose_name='BNC Ports')
    tp = models.IntegerField(default=0, verbose_name='Ethernet Ports')
    installed_in = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True, related_name='nics')

    upload_base = 'nics'

    def get_absolute_url(self):
        return "/nics/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)

    class Meta:
        verbose_name = 'NIC'
        verbose_name_plural = 'NICs'

class Motherboard(Hardware):
    form_factor = models.ForeignKey(Choices.FormFactor, on_delete=models.SET_NULL, null=True)
    socket = models.CharField(max_length=200)
    isa = models.IntegerField(default=0, verbose_name='8-bit ISA Slots')
    isa16 = models.IntegerField(default=0, verbose_name='16-bit ISA Slots')
    vlb = models.IntegerField(default=0, verbose_name='VLB Slots')
    pci = models.IntegerField(default=0, verbose_name='PCI Slots')
    agp = models.IntegerField(default=0, verbose_name='AGP Slots')
    pcie1 = models.IntegerField(default=0, verbose_name='PCIe x1 Slots')
    pcie4 = models.IntegerField(default=0, verbose_name='PCIe x4 Slots')
    pcie8 = models.IntegerField(default=0, verbose_name='PCIe x8 Slots')
    pcie16 = models.IntegerField(default=0, verbose_name='PCIe x16 Slots')
    ram = models.IntegerField(default=0, verbose_name='RAM Slots')
    installed_in = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True, related_name='motherboard')

    upload_base = 'motherboards'

    def get_absolute_url(self):
        return "/motherboards/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)

class PSU(Hardware):
    wattage  = models.IntegerField()
    spec = models.ForeignKey(Choices.PSUSpec, null=True, on_delete=models.SET_NULL)
    minus5v = models.BooleanField(verbose_name='-5v rail')
    molex = models.IntegerField(default=0, verbose_name='Molex Connectors')
    floppy = models.IntegerField(default=0, verbose_name='Floppy Connectors')
    sata = models.IntegerField(default=0, verbose_name='SATA Connectors')
    cpu4pin = models.IntegerField(default=0, verbose_name='4-pin CPU Connectors')
    cpu8pin = models.IntegerField(default=0, verbose_name='8-pin CPU Connectors')
    pcie6pin = models.IntegerField(default=0, verbose_name='6-pin PCIe Connectors')
    pcie8pin = models.IntegerField(default=0, verbose_name='8-pin PCIe Connectors')
    installed_in = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True, related_name='psu')

    upload_base = 'psus'

    def get_absolute_url(self):
        return "/psus/%i" % self.id

    def __str__(self):
        return f'{self.brand} {self.model}'
    
    class Meta:
        verbose_name = 'PSU'
        verbose_name_plural = 'PSUs'

class Drive(Hardware):
    type = models.ForeignKey(Choices.DriveType, on_delete=models.SET_NULL, null=True)
    interface = models.ForeignKey(Choices.DriveInterface, on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField(blank=True, null=True, verbose_name='Capacity (MB)')
    internal = models.BooleanField(default=False)
    installed_in = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True, related_name='drives')

    upload_base= 'drives'

    def get_absolute_url(self):
        return "/drives/%i" % self.id

    def __str__(self):
        return self.name

class Case(Hardware):
    mb_support = models.ManyToManyField(Choices.FormFactor, verbose_name='Motherboard Compatibility')
    installed_in = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, blank=True, related_name='case')

    upload_base = 'cases'

    def get_absolute_url(self):
        return "/cases/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)
    
    class Meta:
        verbose_name = 'Case'

class Proprietary(System):
    upload_base = 'systems/proprietary'

    def get_absolute_url(self):
        return "/systems/%i" % self.id

    def __str__(self):
        return f'{self.brand} {self.name}'
    
    class Meta:
        verbose_name = 'Proprietary System'
        verbose_name_plural = 'Proprietary Systems'

class Micro(Hardware):
    upload_base = 'systems/micros'

    def get_absolute_url(self):
        return "/micros/%i" % self.id

    def __str__(self):
        return f'{self.brand} {self.name}'
    
    class Meta:
        verbose_name = 'Microcomputer'
        verbose_name_plural = 'Microcomputers'

class SBC(models.Model):
    type = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    qty = models.IntegerField(default=1)
    usage = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return "/sbc/%i" % self.id
    
    def __str__(self):
        return '{} {}'.format(self.type, self.model)
    
    class Meta:
        verbose_name = 'Single-board Computer'
        verbose_name_plural = 'Single-board Computers'

class Peripheral(Hardware):
    type = models.ForeignKey(Choices.PeripheralType, on_delete=models.SET_NULL, null=True)
    ports = models.ManyToManyField(Choices.Port, blank=True)

    upload_base = 'peripherals'

    def get_absolute_url(self):
        return "/peripherals/%i" % self.id

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Perhipheral'
        verbose_name_plural = 'Peripherals'

class Cable(Hardware):
    type = models.ForeignKey(Choices.CableType, on_delete=models.SET_NULL, null=True)
    connectors_a = models.ManyToManyField(Choices.Port, related_name='cable_a', verbose_name='Connector(s) (A Side)')
    connectors_b = models.ManyToManyField(Choices.Port, related_name='cable_b', verbose_name='Connector(s) (B Side)')
    quantity = models.IntegerField(default=1)

    upload_base = 'cables'

    def get_absolute_url(self):
        return "/cables/%i" % self.id

    def __str__(self):    
        connectors_a = ', '.join([str(i) for i in self.connectors_a.all()])
        connectors_b = ', '.join([str(i) for i in self.connectors_b.all()])
        if ( connectors_a == connectors_b and self.type.id == 1) or (self.type.id == 2):
            return f'{connectors_a} {self.type}'
        elif connectors_b == 'None':
            return f'{connectors_a} Terminator'
        else:
            return f'{connectors_a} to {connectors_b} {self.type}'

    class Meta:
        verbose_name = 'Cable, Adapter, I/O Bracket'
        verbose_name_plural = 'Cables, Adapters, IO Brackets'