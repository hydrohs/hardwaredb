from django.db import models

# Text choices for various interfaces shared between hardware classes

class Slot(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Slot'
        verbose_name_plural = 'Slots'

class DriveInterface(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Drive Interface'
        verbose_name_plural = 'Drive Interfaces'

class Port(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Port'
        verbose_name_plural = 'Ports'

class PeripheralType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Peripheral Type'
        verbose_name_plural = 'Peripheral Types'

class CableType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Cable Type'
        verbose_name_plural = 'Cable Types'
        
class Peripherals(models.TextChoices):
    SERIAL = 'SERIAL', 'Serial'
    PARALLEL = 'PARALLEL', 'Parallel'
    GAME = 'GAME', 'Gameport'
    JOY = 'JOY', 'Joystick'
    MIDI = 'MIDI', 'Midi'
    ADB = 'ADB', 'ADB'
    FLOPPY = 'FLOPPY', 'Floppy'
    CASS = 'CASS', 'Cassette'
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