from email.policy import default
from django.db import models
from multiselectfield import MultiSelectField

def HumanReadable(calc, value, ram_type):
    # Converts db values into more friendly human readable numbers for display
    def Size():
        if value >= 1024:
            return '{}{}'.format(str(int(value / 1024)), 'GB')
        else:
            return '{}{}'.format(str(int(value)), 'MB')
    
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
    notes = models.TextField(null=True, blank=True)
    top_img = models.ImageField(upload_to='cpus', max_length=255, null=True, blank=True, verbose_name='Top Image')
    bottom_img = models.ImageField(upload_to='cpus', max_length=255, null=True, blank=True, verbose_name='Bottom Image')

    def __str__(self):
        return self.name

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
    class Interface(models.TextChoices):
        ISA = 'ISA', '8-bit ISA'
        ISA16 = 'ISA16', '16-bit ISA'
        VLB = 'VLB', 'VLB'
        PCI = 'PCI', 'PCI'
        AGP = 'AGP', 'AGP'
        AGP2 = 'AGP2', 'AGP 2x'
        AGP4 = 'AGP4', 'AGP 4x'
        AGP8 = 'AGP8', 'AGP 8x'
        PCIE16 = 'PCIE16', 'PCIe x16'

    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    interface = models.CharField(max_length=6, choices=Interface.choices, default=Interface.ISA)
    mda = models.IntegerField(default=0, verbose_name='MDA Ports')
    cga = models.IntegerField(default=0, verbose_name='CGA Ports')
    vga = models.IntegerField(default=0, verbose_name='VGA Ports')
    dvi = models.IntegerField(default=0, verbose_name='DVI Ports')
    hdmi = models.IntegerField(default=0, verbose_name='HDMI Pors')
    dp = models.IntegerField(default=0, verbose_name='Displayport Ports')
    other = models.IntegerField(default=0, verbose_name='Other Ports (Use notes)')
    notes = models.TextField(null=True, blank=True)
    top_img = models.ImageField(upload_to='gpus', max_length=255, null=True, blank=True, verbose_name='Top Image')
    bottom_img = models.ImageField(upload_to='gpus', max_length=255, null=True, blank=True, verbose_name='Bottom Image')
    io_img = models.ImageField(upload_to='gpus', max_length=255, null=True, blank=True, verbose_name='IO Panel')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'GPU'
        verbose_name_plural = 'GPUs'

class SoundCard(models.Model):
    class Interface(models.TextChoices):
        ISA = 'ISA', '8-bit ISA'
        ISA16 = 'ISA16', '16-bit ISA'
        PCI = 'PCI', 'PCI'
        PCIE1 = 'PCIE1', 'PCIe x1'

    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    sb = models.CharField(max_length=200, verbose_name='SB Compatibility')
    interface = models.CharField(max_length=6, choices=Interface.choices, default=Interface.ISA)
    notes = models.TextField(null=True, blank=True)
    top_img = models.ImageField(upload_to='sound_cards', max_length=255, null=True, blank=True, verbose_name='Top Image')
    bottom_img = models.ImageField(upload_to='sound_cards', max_length=255, null=True, blank=True, verbose_name='Bottom Image')
    io_img = models.ImageField(upload_to='sond_cards', max_length=255, null=True, blank=True, verbose_name='IO Panel')

    def __str__(self):
        return self.name

class ExpansionCard(models.Model):
    class Interface(models.TextChoices):
        ISA = 'ISA', '8-bit ISA'
        ISA16 = 'ISA16', '16-bit ISA'
        VLB = 'VLB', 'VLB'
        PCI = 'PCI', 'PCI'
        PCIE1 = 'PCIE1', 'PCIe x1'
        PCIE4 = 'PCIE4', 'PCIe x4'
        PCIE8 = 'PCIE8', 'PCIe x8'
        PCIE16 = 'PCI16', 'PCIe x16'

    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    interface = models.CharField(max_length=6, choices=Interface.choices, default=Interface.ISA)
    io_panel = models.CharField(max_length=255, null=True, blank=True, verbose_name='IO Panel (comma separated)')
    notes = models.TextField(null=True, blank=True)
    top_img = models.ImageField(upload_to='expansion_cards', max_length=255, null=True, blank=True, verbose_name='Top Image')
    bottom_img = models.ImageField(upload_to='expansion_cards', max_length=255, null=True, blank=True, verbose_name='Bottom Image')
    io_img = models.ImageField(upload_to='expansion_cards', max_length=255, null=True, blank=True, verbose_name='IO Panel')

    def __str__(self):
        return self.name

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
    pice1 = models.IntegerField(default=0, verbose_name='PCIe x1 Slots')
    pcie4 = models.IntegerField(default=0, verbose_name='PCIe x4 Slots')
    pcie8 = models.IntegerField(default=0, verbose_name='PCIe x8 Slots')
    pcie16 = models.IntegerField(default=0, verbose_name='PCIe x16 Slots')
    ram = models.IntegerField(default=0, verbose_name='RAM Slots')
    notes = models.TextField(null=True, blank=True)
    top_img = models.ImageField(upload_to='motherboards', max_length=255, null=True, blank=True, verbose_name='Top Image')
    bottom_img = models.ImageField(upload_to='motherboards', max_length=255, null=True, blank=True, verbose_name='Bottom Image')
    io_img = models.ImageField(upload_to='motherboards', max_length=255, null=True, blank=True, verbose_name='IO Panel')

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)

class NIC(models.Model):
    class Interface(models.TextChoices):
        ISA = 'ISA', '8-bit ISA'
        ISA16 = 'ISA16', '16-bit ISA'
        VLB = 'VLB', 'VLB'
        PCI = 'PCI', 'PCI'
        PCIE1 = 'PCIE1', 'PCIe x1'
        PCIE4 = 'PCIE4', 'PCIe x4'
        PCIE8 = 'PCIE8', 'PCIe x8'
        PCIE16 = 'PCI16', 'PCIe x16'
        PCIEM230 = 'M2', 'M.2 2230'

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
    interface = models.CharField(max_length=6, choices=Interface.choices, default=Interface.ISA)
    aui = models.IntegerField(default=0, verbose_name='AUI Ports')
    bnc = models.IntegerField(default=0, verbose_name='BNC Ports')
    tp = models.IntegerField(default=0, verbose_name='Ethernet Ports')
    notes = models.TextField(null=True, blank=True)
    top_img = models.ImageField(upload_to='nics', max_length=255, null=True, blank=True, verbose_name='Top Image')
    bottom_img = models.ImageField(upload_to='nics', max_length=255, null=True, blank=True, verbose_name='Bottom Image')
    io_img = models.ImageField(upload_to='nics', max_length=255, null=True, blank=True, verbose_name='IO Panel')

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)

    class Meta:
        verbose_name = 'NIC'
        verbose_name_plural = 'NICs'

class Case(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    mb_support = MultiSelectField(choices=FormFactor.choices, default=FormFactor.ATX, verbose_name='Motherboard Compatibility')

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

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)
    
    class Meta:
        verbose_name = 'PSU'
        verbose_name_plural = 'PSUs'

class Peripheral(models.Model):
    class Type(models.TextChoices):
        MOUSE = 'M', 'Mouse'
        KB = 'KB', 'Keyboard'
        ZIP = 'ZIP', 'Zip Drive'
        GAME = 'GAME', 'Gamepad'
        JOY = 'JOY', 'Joystick'
        MIDI = 'MIDI', 'Midi'
        SPK = 'SPK', 'Speakers'
        LCD = 'LCD', 'LCD'
        CRT = 'CRT', 'CRT'
        OTHER = 'OTHER', 'Other'

    class Interface(models.TextChoices):
        SERIAL = 'SERIAL', 'Serial'
        PARALLEL = 'PARALLEL', 'Parallel'
        GAME = 'GAME', 'Gameport'
        MIDI = 'MIDI', 'Midi'
        ADB = 'ADB', 'ADB'
        SCSI = 'SCSI', 'SCSI'
        PS2 = 'PS2', 'PS/2'
        USB = 'USB', 'USB'
        PIN = 'PIN', 'Pin Connector'
        MM35 = 'MM35', '3.5MM'
        MM63 = 'MM63', '6.3MM'
        XLR = 'XLR', 'XLR'
        RCA = 'RCA', 'RCA'
        BT = 'BT', 'Bluetooth'
        MDA = 'MDA', 'MDA'
        CGA = 'CGA', 'CGA'
        EGA = 'EGA', 'EGA'
        VGA = 'VGA', 'VGA'
        DVI = 'DVI', 'DVI'
        HDMI = 'HDMI', 'HDMI'
        DP = 'DP', 'DisplayPort'
        OTHER = 'OTHER', 'Other'

    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=Type.choices, default=Type.MOUSE)
    interface = MultiSelectField(choices=Interface.choices, default=Interface.USB)
    notes = models.TextField(null=True, blank=True)
    image_1 = models.ImageField(upload_to='peripherals', max_length=255, null=True, blank=True)
    image_2 = models.ImageField(upload_to='peripherals', max_length=255, null=True, blank=True)
    image_3 = models.ImageField(upload_to='perihperals', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Cables(models.Model):
    class Type(models.TextChoices):
        CABLE = 'CABLE', 'Cable'
        IO = 'IO', 'I/O Bracket'
        ADAPT = 'ADAPT', 'Adapter'

    class Interface(models.TextChoices):
        OTHER = 'OTHER', 'Other'
        DB9SM = 'DB9SM', 'DB-9 Serial Male'
        DB9SF = 'DB9SF', 'DB-9 Serial Female'
        DB25PM = 'DB25PM', 'DB-25 Parallel Male'
        DB25PF = 'DB25PF', 'DB-25 Parallel Female'
        AMPH36M = 'AMPH36M', '36-Pin Amphenol Parallel Male'
        AMPH36F = 'AMPH36F', '36-Pin Amphenol Parallel Female'
        DB25SM = 'DB25SM', 'DB-25 SCSI Male'
        DB25SF = 'DB25SF', 'DB-25 SCSI Female'
        AMPH50M = 'AMPH50M', '50-Pin Amphenol SCSI Male'
        AMPH50F = 'AMPH50F', '50-Pin Amphenol SCSI Female'
        VHDCI68M = 'VHDCI68M', 'VHDCI-68 SCSI Male'
        VHDCI68F = 'VHDCI68F', 'VHDCI-68 SCSI Female'
        DB15GM = 'DB15GM', 'DB-15 Gameport Male'
        DB15GF = 'DB15GF', 'DB-15 Gameport Female'
        USBAM = 'USBAM', 'USB A Male'
        USBAF = 'USBAF', 'USB A Female'
        USBBM = 'USBBM', 'USB B Male'
        USBBF = 'USBBF', 'USB B Female'
        USBMICROBM = 'USBMICROBM', 'USB Micro B Male'
        USBMICROBF = 'USBMICROBF', 'USB Micro B Female'
        USBMINIBM = 'USBMINIBM', 'USB Mini B Male'
        USBMINIBF = 'USBMINIBF', 'USB Mini B Female'
        DIN5M = 'DIN5M', '5-Pin DIN Male'
        DIN5F = 'DIN5F', '5-Pin DIN Female'
        ADBM = 'ADBM', 'ADB Male'
        ADBF = 'ADBF', 'ADB Female'
        PS2M = 'PS2M', 'PS/2 Male'
        PS2F = 'PS2F', 'PS/2 Female'
        PIN4 = 'PIN4', '4-Pin Connector'
        PIN6 = 'PIN6', '6-Pin Connector'
        PIN8 = 'PIN8', '8-Pin Connector'
        MM35M = 'MM35M', '3.5MM Male'
        MM35F = 'MM35F', '3.5MM Female'
        MM63M = 'MM63M', '6.3MM Male'
        MM63F = 'MM63F', '6.3MM Female'
        XLRM = 'XLRM', 'XLR Male'
        XLRF = 'XLRF', 'XLR Female'
        RCAM = 'RCAM', 'RCA Male'
        RCAF = 'RCAF', 'RCA Female'
        MDAM = 'MDAM', 'DB-9 MDA Male'
        MDAF = 'MDAF', 'DB-9 MDA Female'
        CGAM = 'CGAM', 'DB-9 CGA Male'
        CGAF = 'CGAF', 'DB-9 CGA Female'
        EGAM = 'EGAM', 'DB-9 EGA Male'
        EGAF = 'EGAF', 'DB-9 EGA Female'
        VGAM = 'VGAM', 'DB-15 VGA Male'
        VGAF = 'VGAF', 'DB-15 VGA Female'
        DVIDDM = 'DVIDDM', 'DVI-D Dual-Link Male'
        DVIDDF = 'DVIDDF', 'DVI-D Dual-Link Female'
        DVIDSM = 'DVIDSM', 'DVI-D Single-Link Male'
        DVIDSF = 'DVIDSF', 'DVI-D Single-Link Female'
        DVIIDM = 'DVIIDM', 'DVI-I Dual-Link Male'
        DVIIDF = 'DVIIDF', 'DVI-I Dual-Link Female'
        DVIISM = 'DVIISM', 'DVI-I Single-Link Male'
        DVIISF = 'DVIISF', 'DVI-I Single-Link Female'
        DVIAM = 'DVIAM', 'DVI-A Male'
        DVIAF = 'DVIAF', 'DVI-A Female'
        HDMIM = 'HDMIM', 'HDMI Male'
        HDMIF = 'HDMIF', 'HDMI Female'
        MINIHDMIM = 'MINIHDMIM', 'Mini HDMI Male'
        MINIHDMIF = 'MINIHDMIF', 'Mini HDMI Female'
        MICROHDMIM = 'MICROHDMIM', 'Micro HDMI Male'
        MICROHDMIF = 'MICROHDMIF', 'Micro HDMI Female'
        DPM = 'DPM', 'DisplayPort Male'
        DPF = 'DPF', 'DisplayPort Female'
        MINIDPM = 'MINIDPM', 'Mini DisplayPort Male'
        MINIDPF = 'MINIDPF', 'Mini DisplayPort Female'

    type = models.CharField(max_length=10, choices=Type.choices, default=Type.CABLE)
    name = models.CharField(max_length=200)
    interface_a = MultiSelectField(choices=Interface.choices, default=Interface.OTHER, verbose_name="Interface A")
    interface_b = MultiSelectField(choices=Interface.choices, default=Interface.OTHER, verbose_name="Interface B")
    quantity = models.IntegerField(default=1)
    notes = models.TextField(null=True, blank=True)
    image_1 = models.ImageField(upload_to='cables', max_length=255, null=True, blank=True)
    image_2 = models.ImageField(upload_to='cables', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cable, Adapter, I/O Bracket'
        verbose_name_plural = 'Cables, Adapters, IO Brackets'