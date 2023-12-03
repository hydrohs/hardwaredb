from django.db import models
from polymorphic.models import PolymorphicModel
from .interfaces import *
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
    model = instance.part.model
    pk = instance.part.pk
    extension = os.path.splitext(filename)[1]
    return f'{base}/{brand}_{model}_{pk}/{instance.name}{extension}'

class FormFactor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

class Hardware(PolymorphicModel):
    brand = models.CharField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path)
    part = models.ForeignKey(Hardware, related_name='images', on_delete=models.CASCADE)

class CPU(Hardware):
    speed = models.IntegerField()
    socket = models.CharField(max_length=200)
    cores = models.IntegerField()
    hyperthreading = models.BooleanField()
    cpu_world = models.TextField(null=True, blank=True)

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
    class Type(models.TextChoices):
        FPM = 'FPM', 'FPM'
        EDO = 'EDO', 'EDO'
        SDRAM = 'SDRAM', 'SDRAM'
        DDR = 'DDR1', 'DDR'
        DDR2 = 'DDR2', 'DDR2'
        DDR3 = 'DDR3', 'DDR3'
        DDR4 = 'DDR4', 'DDR4'
        DDR5 = 'DDR5', 'DDR5'

    class Interface(models.TextChoices):
        SIMM30 = 'SIMM30', '30-pin SIMM'
        SIMM72 = 'SIMM72', '72-pin SIMM'
        DIMM = 'DIMM', 'DIMM'
        SODIMM = 'SODIMM', 'SO-DIMM'

    type = models.CharField(max_length=5, choices=Type.choices, default=Type.FPM)
    interface = models.CharField(max_length=6, choices=Interface.choices, default=Interface.SIMM30)
    size = models.IntegerField(verbose_name='Size (MB)')
    speed = models.IntegerField(verbose_name='Speed (ns or MHz)')
    ecc = models.BooleanField(verbose_name='ECC')

    def get_absolute_url(self):
        return "/ram/%i" % self.id

    def __str__(self):
        if self.ecc:
            is_ecc = 'ECC'
        else:
            is_ecc = ''
        
        return '{} {} {} {} {}'.format(HumanReadable('size', self.size, ''), HumanReadable('ram', self.speed, self.type), self.get_type_display(), is_ecc, self.get_interface_display())

    class Meta:
        verbose_name = 'RAM'
        verbose_name_plural = 'RAM'

class GPU(Hardware):
    gpu_brand = models.CharField(max_length=32, verbose_name='GPU')
    interface = models.ForeignKey(Slot, on_delete=models.SET_NULL, null=True)
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
    interface = models.ForeignKey(Slot, on_delete=models.SET_NULL, null=True)

    upload_base = 'sound_cards'

    def get_absolute_url(self):
        return "/sound_cards/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.name)

class ExpansionCard(Hardware):
    interface = models.ForeignKey(Slot, on_delete=models.SET_NULL, null=True)
    io_panel = models.CharField(max_length=255, null=True, blank=True, verbose_name='IO Panel (comma separated)')

    upload_base = 'expansion_cards'

    def get_absolute_url(self):
        return "/expansion_cards/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.name)
    
class NIC(Hardware):
    class Speed(models.TextChoices):
        A = 'A'
        B = 'B'
        G = 'G'
        N = 'N'
        AC = 'AC', 'AC'
        AX = 'AX', 'AX'
        TEN = '10', '10 Megabit'
        HUN = '100', '10/100 Megabit'
        GIG = '1000', 'Gigabit'
        TWOFIVE = '2500', '2.5 Gigabit'
        TENG = '10G', '10 Gigabit'
    
    wireless = models.BooleanField()
    speed = models.CharField(max_length=7, choices=Speed.choices, default=Speed.TEN)
    interface = models.ForeignKey(Slot, on_delete=models.SET_NULL, null=True)
    aui = models.IntegerField(default=0, verbose_name='AUI Ports')
    bnc = models.IntegerField(default=0, verbose_name='BNC Ports')
    tp = models.IntegerField(default=0, verbose_name='Ethernet Ports')

    upload_base = 'nics'

    def get_absolute_url(self):
        return "/nics/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)

    class Meta:
        verbose_name = 'NIC'
        verbose_name_plural = 'NICs'

class Motherboard(Hardware):
    form_factor = models.ForeignKey(FormFactor, on_delete=models.SET_NULL, null=True)
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

    upload_base = 'motherboards'

    def get_absolute_url(self):
        return "/motherboards/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)

class PSU(Hardware):
    class Spec(models.TextChoices):
        PROP = 'PROP', 'Proprietary'
        AT = 'AT', 'AT'
        ATX20 = 'AXT20', '20-pin ATX'
        ATX24 = 'ATX24', '24-pin ATX'
        ATX2_4 = 'ATX2_4', '20+4-pin ATX'

    wattage  = models.IntegerField()
    spec = models.CharField(max_length=6, choices=Spec.choices, default=Spec.AT)
    minus5v = models.BooleanField(verbose_name='-5v rail')
    molex = models.IntegerField(default=0, verbose_name='Molex Connectors')
    floppy = models.IntegerField(default=0, verbose_name='Floppy Connectors')
    sata = models.IntegerField(default=0, verbose_name='SATA Connectors')
    cpu4pin = models.IntegerField(default=0, verbose_name='4-pin CPU Connectors')
    cpu8pin = models.IntegerField(default=0, verbose_name='8-pin CPU Connectors')
    pcie6pin = models.IntegerField(default=0, verbose_name='6-pin PCIe Connectors')
    pcie8pin = models.IntegerField(default=0, verbose_name='8-pin PCIe Connectors')

    upload_base = 'psus'

    def get_absolute_url(self):
        return "/psus/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)
    
    class Meta:
        verbose_name = 'PSU'
        verbose_name_plural = 'PSUs'

class Drive(Hardware):
    class Type(models.TextChoices):
        FLOPPY5 = 'FLOPPY5', '5.25" Floppy'
        FLOPPY3 = 'FLOPPY3', '3.5" Floppy'
        ZIP = 'ZIP', 'Zip'
        CD = 'CD', 'CD'
        DVD = 'DVD', 'DVD'
        BR = 'BR', 'Bluray'
        HDD = 'HDD', 'HDD'
        SSD = 'SSD', 'SSD'
    
    type = models.CharField(max_length=10, choices=Type.choices, default=Type.FLOPPY5)
    interface = models.ForeignKey(DriveInterface, on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField(blank=True, null=True, verbose_name='Capacity (MB)')

    upload_base= 'drives'

    def get_absolute_url(self):
        return "/drives/%i" % self.id

    def __str__(self):
        return self.name

class Case(Hardware):
    mb_support = models.ManyToManyField(FormFactor, verbose_name='Motherboard Compatibility')

    upload_base = 'cases'

    def get_absolute_url(self):
        return "/cases/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)
    
    class Meta:
        verbose_name = 'Case'

class MicroProp(Hardware):
    class Type(models.TextChoices):
        MICRO = 'MICRO', 'Microcomputer'
        PROP = 'PROP', 'Proprietary'

    type = models.CharField(max_length=20, choices=Type.choices, default=Type.PROP)

    upload_base = 'micros_proprietary'

    def get_absolute_url(self):
        return "/microprop/%i" % self.id

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Microcomputer/Proprietary System'
        verbose_name_plural = 'Microcomputers/Proprietary Systems'

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
    type = models.ForeignKey(PeripheralType, on_delete=models.SET_NULL, null=True)
    ports = models.ManyToManyField(Port, blank=True)

    upload_base = 'peripherals'

    def get_absolute_url(self):
        return "/peripherals/%i" % self.id

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Perhipheral'
        verbose_name_plural = 'Peripherals'

class Cable(Hardware):
    type = models.ForeignKey(CableType, on_delete=models.SET_NULL, null=True)
    connectors_a = models.ManyToManyField(Port, related_name='cable_a', verbose_name='Connector(s) (A Side)')
    connectors_b = models.ManyToManyField(Port, related_name='cable_b', verbose_name='Connector(s) (B Side)')
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