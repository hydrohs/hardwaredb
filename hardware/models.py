from django import forms
from django.db import models
from multiselectfield import MultiSelectField
from .interfaces import *

def HumanReadable(calc, value, ram_type):
    # Converts db values into more friendly human readable numbers for display
    def Size():
        if value >= 1048576:
            size = value / 1048576
            return '{}{}'.format(str(int(size) if float(size).is_integer() else size), 'TB')
        elif value >= 1024:
            size = value / 1024
            return '{}{}'.format(str(int(size) if float(size).is_integer() else size), 'GB')
        else:
            return '{}{}'.format(str(value), 'MB')
    
    def CpuFreq():
        if value >= 1000:
            return '{}{}'.format(str(value / 1000), 'GHz')
        else:
            return '{}{}'.format(value, 'MHz')
    
    def RamSpeed():
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

class FormFactor(models.TextChoices):
    # Both motherboards and cases should have access to the same
    # form factors so this is global
        AT = 'AT', 'AT'
        BABY_AT = 'BABYAT', 'Baby AT'
        ATX = 'ATX', 'ATX'
        EATX = 'EATX', 'E-ATX'
        MATX = 'MATX', 'Micro ATX'
        ITX = 'ITX', 'Mini ITX'
        PROP = 'PROP', 'Proprietary'

class CPU(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    speed = models.IntegerField()
    socket = models.CharField(max_length=200)
    cores = models.IntegerField()
    hyperthreading = models.BooleanField()
    cpu_world = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    top_img = models.ImageField(upload_to='cpus', max_length=255, null=True, blank=True, verbose_name='Top Image')
    bottom_img = models.ImageField(upload_to='cpus', max_length=255, null=True, blank=True, verbose_name='Bottom Image')

    def get_absolute_url(self):
        return "/cpus/%i" % self.id

    def __str__(self):
        return self.name

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

class GPU(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    interface = models.CharField(max_length=10, choices=Slots.choices, default=Slots.ISA)
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
    notes = models.TextField(null=True, blank=True)
    top_img = models.ImageField(upload_to='gpus', max_length=255, null=True, blank=True, verbose_name='Top Image')
    bottom_img = models.ImageField(upload_to='gpus', max_length=255, null=True, blank=True, verbose_name='Bottom Image')
    io_img = models.ImageField(upload_to='gpus', max_length=255, null=True, blank=True, verbose_name='IO Panel')

    def get_absolute_url(self):
        return "/gpus/%i" % self.id

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'GPU'
        verbose_name_plural = 'GPUs'

class SoundCard(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    sb = models.CharField(max_length=200, verbose_name='SB Compatibility')
    interface = models.CharField(max_length=10, choices=Slots.choices, default=Slots.ISA)
    notes = models.TextField(null=True, blank=True)
    top_img = models.ImageField(upload_to='sound_cards', max_length=255, null=True, blank=True, verbose_name='Top Image')
    bottom_img = models.ImageField(upload_to='sound_cards', max_length=255, null=True, blank=True, verbose_name='Bottom Image')
    io_img = models.ImageField(upload_to='sond_cards', max_length=255, null=True, blank=True, verbose_name='IO Panel')

    def get_absolute_url(self):
        return "/sound_cards/%i" % self.id

    def __str__(self):
        return self.name

class ExpansionCard(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    interface = models.CharField(max_length=10, choices=Slots.choices, default=Slots.ISA)
    io_panel = models.CharField(max_length=255, null=True, blank=True, verbose_name='IO Panel (comma separated)')
    notes = models.TextField(null=True, blank=True)
    top_img = models.ImageField(upload_to='expansion_cards', max_length=255, null=True, blank=True, verbose_name='Top Image')
    bottom_img = models.ImageField(upload_to='expansion_cards', max_length=255, null=True, blank=True, verbose_name='Bottom Image')
    io_img = models.ImageField(upload_to='expansion_cards', max_length=255, null=True, blank=True, verbose_name='IO Panel')

    def get_absolute_url(self):
        return "/expansion_cards/%i" % self.id

    def __str__(self):
        return self.name

class NIC(models.Model):

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
    
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    wireless = models.BooleanField()
    speed = models.CharField(max_length=7, choices=Speed.choices, default=Speed.TEN)
    interface = models.CharField(max_length=6, choices=Slots.choices, default=Slots.ISA)
    aui = models.IntegerField(default=0, verbose_name='AUI Ports')
    bnc = models.IntegerField(default=0, verbose_name='BNC Ports')
    tp = models.IntegerField(default=0, verbose_name='Ethernet Ports')
    notes = models.TextField(null=True, blank=True)
    top_img = models.ImageField(upload_to='nics', max_length=255, null=True, blank=True, verbose_name='Top Image')
    bottom_img = models.ImageField(upload_to='nics', max_length=255, null=True, blank=True, verbose_name='Bottom Image')
    io_img = models.ImageField(upload_to='nics', max_length=255, null=True, blank=True, verbose_name='IO Panel')

    def get_absolute_url(self):
        return "/nics/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)

    class Meta:
        verbose_name = 'NIC'
        verbose_name_plural = 'NICs'

class Motherboard(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    form_factor = models.CharField(max_length=6, choices=FormFactor.choices, default=FormFactor.ATX)
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
    notes = models.TextField(null=True, blank=True)
    top_img = models.ImageField(upload_to='motherboards', max_length=255, null=True, blank=True, verbose_name='Top Image')
    bottom_img = models.ImageField(upload_to='motherboards', max_length=255, null=True, blank=True, verbose_name='Bottom Image')
    io_img = models.ImageField(upload_to='motherboards', max_length=255, null=True, blank=True, verbose_name='IO Panel')

    def get_absolute_url(self):
        return "/motherboards/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)

class PSU(models.Model):
    class Spec(models.TextChoices):
        AT = 'AT', 'AT'
        ATX20 = 'AXT20', '20-pin ATX'
        ATX24 = 'ATX24', '24-pin ATX'
        ATX2_4 = 'ATX2_4', '20+4-pin ATX'

    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
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
    notes = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='psus', max_length=255, null=True, blank=True)

    def get_absolute_url(self):
        return "/psus/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)
    
    class Meta:
        verbose_name = 'PSU'
        verbose_name_plural = 'PSUs'

class Drive(models.Model):
    class Type(models.TextChoices):
        FLOPPY5 = 'FLOPPY5', '5.25" Floppy'
        FLOPPY3 = 'FLOPPY3', '3.5" Floppy'
        ZIP = 'ZIP', 'Zip'
        CD = 'CD', 'CD'
        DVD = 'DVD', 'DVD'
        BR = 'BR', 'Bluray'
        HDD = 'HDD', 'HDD'
        SSD = 'SSD', 'SSD'
    
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=Type.choices, default=Type.FLOPPY5)
    interface = models.CharField(max_length=20, choices=Drives.choices, default=Drives.FLOPPYEDGE)
    capacity = models.IntegerField(blank=True, null=True, verbose_name='Capacity (MB)')
    top_img = models.ImageField(upload_to='drives', max_length=255, null=True, blank=True)
    bezel_img = models.ImageField(upload_to='drives', max_length=255, null=True, blank=True)
    rear_img = models.ImageField(upload_to='drives', max_length=255, null=True, blank=True)

    def get_absolute_url(self):
        return "/drives/%i" % self.id

    def __str__(self):
        return self.name

class Case(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    mb_support = MultiSelectField(choices=FormFactor.choices, default=FormFactor.ATX, verbose_name='Motherboard Compatibility')
    image_1 = models.ImageField(upload_to='case', max_length=255, null=True, blank=True)
    image_2 = models.ImageField(upload_to='cases', max_length=255, null=True, blank=True)
    image_3 = models.ImageField(upload_to='cases', max_length=255, null=True, blank=True)

    def get_absolute_url(self):
        return "/cases/%i" % self.id

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)

class System(models.Model):
    name = models.CharField(max_length=200)
    os = models.CharField(max_length=200, blank=True, verbose_name='Operating System')
    cpu1 = models.OneToOneField(CPU, on_delete=models.SET_NULL, null=True, blank=True, related_name='cpu1', verbose_name='CPU')
    cpu2 = models.OneToOneField(CPU, on_delete=models.SET_NULL, null=True, blank=True, related_name='cpu2', verbose_name='CPU')
    ram1 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram1', verbose_name='RAM')
    ram2 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram2', verbose_name='RAM')
    ram3 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram3', verbose_name='RAM')
    ram4 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram4', verbose_name='RAM')
    ram5 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram5', verbose_name='RAM')
    ram6 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram6', verbose_name='RAM')
    ram7 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram7', verbose_name='RAM')
    ram8 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram8', verbose_name='RAM')
    ram9 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram9', verbose_name='RAM')
    ram10 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram10', verbose_name='RAM')
    ram11 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram11', verbose_name='RAM')
    ram12 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram12', verbose_name='RAM')
    ram13 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram13', verbose_name='RAM')
    ram14 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram14', verbose_name='RAM')
    ram15 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram15', verbose_name='RAM')
    ram16 = models.OneToOneField(RAM, on_delete=models.SET_NULL, null=True, blank=True, related_name='ram16', verbose_name='RAM')
    motherboard = models.OneToOneField(Motherboard, on_delete=models.SET_NULL, null=True, blank=True, related_name='motherboard')
    gpu1 = models.OneToOneField(GPU, on_delete=models.SET_NULL, null=True, blank=True, related_name='gpu1', verbose_name='GPU')
    gpu2 = models.OneToOneField(GPU, on_delete=models.SET_NULL, null=True, blank=True, related_name='gpu2', verbose_name='GPU')
    soundcard1 = models.OneToOneField(SoundCard, on_delete=models.SET_NULL, null=True, blank=True, related_name='soundcard1', verbose_name='Sound Card')
    soundcard2 = models.OneToOneField(SoundCard, on_delete=models.SET_NULL, null=True, blank=True, related_name='soundcard2', verbose_name='Sound Card')
    nic = models.OneToOneField(NIC, on_delete=models.SET_NULL, null=True, blank=True, related_name='nic', verbose_name='NIC')
    expansion1 = models.OneToOneField(ExpansionCard, on_delete=models.SET_NULL, null=True, blank=True, related_name='expansion1', verbose_name='Expansion Card')
    expansion2 = models.OneToOneField(ExpansionCard, on_delete=models.SET_NULL, null=True, blank=True, related_name='expansion2', verbose_name='Expansion Card')
    expansion3 = models.OneToOneField(ExpansionCard, on_delete=models.SET_NULL, null=True, blank=True, related_name='expansion3', verbose_name='Expansion Card')
    expansion4 = models.OneToOneField(ExpansionCard, on_delete=models.SET_NULL, null=True, blank=True, related_name='expansion4', verbose_name='Expansion Card')
    expansion5 = models.OneToOneField(ExpansionCard, on_delete=models.SET_NULL, null=True, blank=True, related_name='expansion5', verbose_name='Expansion Card')
    expansion6 = models.OneToOneField(ExpansionCard, on_delete=models.SET_NULL, null=True, blank=True, related_name='expansion6', verbose_name='Expansion Card')
    psu = models.OneToOneField(PSU, on_delete=models.SET_NULL, null=True, blank=True, related_name='psu', verbose_name='PSU')
    drive1 = models.OneToOneField(Drive, on_delete=models.SET_NULL, null=True, blank=True, related_name='drive1', verbose_name='Drive')
    drive2 = models.OneToOneField(Drive, on_delete=models.SET_NULL, null=True, blank=True, related_name='drive2', verbose_name='Drive')
    drive3 = models.OneToOneField(Drive, on_delete=models.SET_NULL, null=True, blank=True, related_name='drive3', verbose_name='Drive')
    drive4 = models.OneToOneField(Drive, on_delete=models.SET_NULL, null=True, blank=True, related_name='drive4', verbose_name='Drive')
    drive5 = models.OneToOneField(Drive, on_delete=models.SET_NULL, null=True, blank=True, related_name='drive5', verbose_name='Drive')
    drive6 = models.OneToOneField(Drive, on_delete=models.SET_NULL, null=True, blank=True, related_name='drive6', verbose_name='Drive')
    drive7 = models.OneToOneField(Drive, on_delete=models.SET_NULL, null=True, blank=True, related_name='drive7', verbose_name='Drive')
    drive8 = models.OneToOneField(Drive, on_delete=models.SET_NULL, null=True, blank=True, related_name='drive8', verbose_name='Drive')
    case = models.OneToOneField(Case, on_delete=models.SET_NULL, null=True, blank=True, related_name='case')
    image_1 = models.ImageField(upload_to='systems', max_length=255, null=True, blank=True)
    image_2 = models.ImageField(upload_to='systems', max_length=255, null=True, blank=True)
    image_3 = models.ImageField(upload_to='systems', max_length=255, null=True, blank=True)
    image_4 = models.ImageField(upload_to='systems', max_length=255, null=True, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/systems/%i" % self.id

    def get_ram(self):
        fields = (self.ram1, self.ram2, self.ram3, self.ram4, self.ram5, self.ram6)
        ram = 0
        for f in fields:
            if f:
                ram += f.size
        
        return '{} {} {}'.format(
            HumanReadable('size', ram, ''),
            self.ram1.get_type_display(),
            HumanReadable('ram', self.ram1.speed, self.ram1.get_type_display())
            )

class Peripheral(models.Model):
    class Type(models.TextChoices):
        MOUSE = 'M', 'Mouse'
        KB = 'KB', 'Keyboard'
        ZIP = 'ZIP', 'Zip Drive'
        FLOPPY = 'FLOPPY', 'Floppy Drive'
        HDD = 'HDD', 'Hard Drive'
        DISC = 'DISC', 'Disc Drive'
        GAME = 'GAME', 'Gamepad'
        JOY = 'JOY', 'Joystick'
        MIDI = 'MIDI', 'Midi'
        SPK = 'SPK', 'Speakers'
        LCD = 'LCD', 'LCD'
        CRT = 'CRT', 'CRT'
        OTHER = 'OTHER', 'Other'

    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=Type.choices, default=Type.MOUSE)
    interface = MultiSelectField(choices=Peripherals.choices, default=Peripherals.USB)
    notes = models.TextField(null=True, blank=True)
    image_1 = models.ImageField(upload_to='peripherals', max_length=255, null=True, blank=True)
    image_2 = models.ImageField(upload_to='peripherals', max_length=255, null=True, blank=True)
    image_3 = models.ImageField(upload_to='peripherals', max_length=255, null=True, blank=True)

    def get_absolute_url(self):
        return "/peripherals/%i" % self.id

    def __str__(self):
        return self.name

class Cable(models.Model):
    class Type(models.TextChoices):
        CABLE = 'CABLE', 'Cable'
        IO = 'IO', 'I/O Bracket'
        ADAPT = 'ADAPT', 'Adapter'

    type = models.CharField(max_length=10, choices=Type.choices, default=Type.CABLE)
    name = models.CharField(max_length=200)
    interface_a = MultiSelectField(choices=Cables.choices, default=Cables.OTHER, verbose_name="Interface A")
    interface_b = MultiSelectField(choices=Cables.choices, default=Cables.OTHER, verbose_name="Interface B")
    quantity = models.IntegerField(default=1)
    notes = models.TextField(null=True, blank=True)
    image_1 = models.ImageField(upload_to='cables', max_length=255, null=True, blank=True)
    image_2 = models.ImageField(upload_to='cables', max_length=255, null=True, blank=True)

    def get_absolute_url(self):
        return "/cables/%i" % self.id

    def __str__(self):
        return '{} to {} {}'.format(self.interface_a, self.interface_b, self.get_type_display())

    class Meta:
        verbose_name = 'Cable, Adapter, I/O Bracket'
        verbose_name_plural = 'Cables, Adapters, IO Brackets'