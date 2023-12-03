from django.db import models

# Connectors/ports/slots shared between hardware classes

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