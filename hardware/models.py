from django.db import models
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible

@deconstructible
class GetImageName(object):

    def __init__(self, base_path, uuid_folder, image_name):
        self.base_path = base_path
        self.uuid = uuid_folder
        self.image_name = image_name

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(self.image_name, ext)
        return os.path.join(self.base_path, self.uuid, filename)


class CPU(models.Model):
    tempid = uuid4()
    id = models.UUIDField(primary_key=True, default=tempid, editable=False)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    speed = models.IntegerField()
    socket = models.CharField(max_length=200)
    cores = models.IntegerField()
    hyperthreading = models.BooleanField()
    notes = models.TextField(null=True, blank=True)
    get_path = GetImageName('cpus', str(tempid), 'top')
    top_img = models.ImageField(upload_to=get_path, max_length=255, null=True, blank=True)
    get_path = GetImageName('cpus', str(tempid), 'bottom')
    bottom_img = models.ImageField(upload_to=get_path, max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

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

    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    type = models.CharField(max_length=5, choices=Type.choices, default=Type.FPM)
    interface = models.CharField(max_length=6, choices=Interface.choices, default=Interface.SIMM30)
    size = models.IntegerField()
    speed = models.IntegerField()
    ecc = models.BooleanField