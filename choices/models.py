from django.db import models

from django.db import models

# Connectors/ports/slots shared between hardware classes

class FormFactor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

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

class DriveType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Drive Type'
        verbose_name_plural = 'Drive Types'

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

class PSUSpec(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Power Supply Specification'
        verbose_name_plural = 'Power Supply Specifications'

class NetSpeed(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Networking Speed'
        verbose_name_plural = 'Networking Speeds'

class RAMType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'RAM Type'
        verbose_name_plural = 'RAM Types'

class RAMInterface(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'RAM Interface'
        verbose_name_plural = 'RAM Interfaces'