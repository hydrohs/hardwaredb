from django.db import models

class CPU(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    speed = models.IntegerField()
    socket = models.CharField(max_length=200)
    cores = models.IntegerField()
    hyperthreading = models.BooleanField()
    notes = models.TextField(null=True, blank=True)
    top_img = models.ImageField(upload_to='cpus', max_length=255, null=True, blank=True)
    bottom_img = models.ImageField(upload_to='cpus', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name