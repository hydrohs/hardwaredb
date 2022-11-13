from django.db import models

# Text choices for various interfaces shared between hardware classes

class Slots(models.TextChoices):
    ISA = 'ISA', '8-bit ISA'
    ISA16 = 'ISA16', '16-bit ISA'
    VLB = 'VLB', 'VLB'
    PCI = 'PCI', 'PCI'
    AGP = 'AGP', 'AGP'
    AGP2 = 'AGP2', 'AGP 2x'
    AGP4 = 'AGP4', 'AGP 4x'
    AGP8 = 'AGP8', 'AGP 8x'
    PCIE1 = 'PCIE1', 'PCIe x1'
    PCIE4 = 'PCIE4', 'PCIe x4'
    PCIE8 = 'PCIE8', 'PCIe x8'
    PCIE16 = 'PCIE16', 'PCIe x16'
    PCIEM230 = 'M2', 'M.2 2230'

class Drives(models.TextChoices):
    FLOPPYEDGE = 'FLOPPYEDGE', '34-Pin Floppy Edge'
    FLOPPY = 'FLOPPY', '34-Pin Floppy'
    IDE = 'IDE', 'IDE'
    SCSI = 'SCSI', 'SCSI'
    SATA = 'SATA', 'SATA'
    M240 = 'M240', 'M.2 2240'
    M280 = 'M280', 'M.2 2280'

class Peripherals(models.TextChoices):
    SERIAL = 'SERIAL', 'Serial'
    PARALLEL = 'PARALLEL', 'Parallel'
    GAME = 'GAME', 'Gameport'
    MIDI = 'MIDI', 'Midi'
    ADB = 'ADB', 'ADB'
    FLOPPY = 'FLOPPY', 'Apple Floppy'
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

class Cables(models.TextChoices):
    OTHER = 'OTHER', 'Other'
    PROP = 'PROP', 'Proprietary'
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
    DA15GM = 'DA15GM', 'DA-15 Gameport Male'
    DA15GF = 'DA15GF', 'DA-15 Gameport Female'
    USBAM = 'USBAM', 'USB A Male'
    USBAF = 'USBAF', 'USB A Female'
    USBBM = 'USBBM', 'USB B Male'
    USBBF = 'USBBF', 'USB B Female'
    USBMICROBM = 'USBMICROBM', 'USB Micro B Male'
    USBMICROBF = 'USBMICROBF', 'USB Micro B Female'
    USBMINIBM = 'USBMINIBM', 'USB Mini B Male'
    USBMINIBF = 'USBMINIBF', 'USB Mini B Female'
    USBCM = 'USBCM', 'USB-C Male'
    USBCF = 'USBCF', 'USB-C Female'
    DIN5M = 'DIN5M', '5-Pin DIN Male'
    DIN5F = 'DIN5F', '5-Pin DIN Female'
    MINIDIN3M = 'MINIDIN3M', '3-Pin Mini-DIN Male'
    MINIDIN3F = 'MINIDIN4F', '3-Pin Mini-DIN Female'
    MINIDIN7M = 'MINIDIN7M', '7-Pin Mini-DIN Male'
    MINIDIN7F = 'MINIDIN7F', '7-Pin Mini-DIN Female'
    MINIDIN9M = 'MINIDIN9M', '9-Pin Mini-DIN Male'
    MINIDIN9F = 'MINIDIN9F', '9-Pin Mini-DIN Female'
    ADBM = 'ADBM', 'ADB Male'
    ADBF = 'ADBF', 'ADB Female'
    PS2M = 'PS2M', 'PS/2 Male'
    PS2F = 'PS2F', 'PS/2 Female'
    PIN4 = 'PIN4', '4-Pin Connector'
    PIN6 = 'PIN6', '6-Pin Connector'
    PIN8 = 'PIN8', '8-Pin Connector'
    PIN10 = 'PIN10', '10-Pin Connector'
    PIN16 = 'PIN16', '16-Pin Connector'
    PIN26 = 'PIN26', '26-Pin Connector'
    PIN34 = 'PIN34', '34-Pin Connector'
    PIN40 = 'PIN40', '40-Pin Connector'
    PIN44 = 'PIN44', '44-Pin Connector'
    PIN50 = 'PIN50', '50-Pin Connector'
    EDGE34 = 'EDGE34', '34-Pin Edge Connector'
    SATAM = 'SATAM', 'SATA Male'
    SATAF = 'SATAF', 'SATA Female'
    MM25M = 'MM25M', '2.5MM Male'
    MM25F = 'MM25F', '2.5MM Female'
    MM35M = 'MM35M', '3.5MM Male'
    MM35F = 'MM35F', '3.5MM Female'
    MM63M = 'MM63M', '6.3MM Male'
    MM63F = 'MM63F', '6.3MM Female'
    TOSLINKM = 'TOSLINKM', 'Toslink Male'
    TOSLINKF = 'TOSLINKF', 'Toslink Female'
    XLRM = 'XLRM', 'XLR Male'
    XLRF = 'XLRF', 'XLR Female'
    RCAM = 'RCAM', 'RCA Male'
    RCAF = 'RCAF', 'RCA Female'
    COMPM = 'COMPM', 'Composite Male'
    COMPF = 'COMPF', 'Composite Female'
    SVIDM = 'SVIDM', 'S-Video Male'
    SVIDF = 'SVIDF', 'S-Video Female'
    COMPOM = 'COMPOM', 'Component Male'
    COMPOF = 'COMPOF', 'Component Female'
    BNCM = 'BNCM', 'BNC Male'
    BNCF = 'BNCF', 'BCN Female'
    COAXM = 'COAXM', 'Coaxial Male'
    COAXF = 'COAXF', 'Coaxial Female'
    SMAM = 'SMAM', 'SMA Male'
    SMAF = 'SMAF', 'SMA Female'
    MDAM = 'MDAM', 'DB-9 MDA Male'
    MDAF = 'MDAF', 'DB-9 MDA Female'
    CGAM = 'CGAM', 'DB-9 CGA Male'
    CGAF = 'CGAF', 'DB-9 CGA Female'
    EGAM = 'EGAM', 'DB-9 EGA Male'
    EGAF = 'EGAF', 'DB-9 EGA Female'
    VGAM = 'VGAM', 'DE-15 VGA Male'
    VGAF = 'VGAF', 'DE-15 VGA Female'
    APPLEVIDM = 'APPLEVIDM', 'DA-15 Apple Video Male'
    APPLEVIDF = 'APPLEVIDF', 'DA-15 Apple Video Female'
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
    MOLEXM = 'MOLEXM', '4-Pin Molex Male'
    MOLEXF = 'MOLEXF', '4-Pin Molex Female'
    BERGM = 'BERGM', 'Berg Male'
    BERGF = 'BERGF', 'Berg Female'
    SATAPM = 'SATAPM', 'SATA Power Male'
    SATAPF = 'SATAPF', 'SATA Power Female'
    PEG6M = 'PEG6M', '6-Pin PEG Male'
    PEG6F = 'PEG6F', '6-Pin PEG Female'
    PEG8M = 'PEG8M', '8-Pin PEG Male'
    PEG8F = 'PEG8F', '8-Pin PEG Female'