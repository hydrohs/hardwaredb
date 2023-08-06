import django_tables2 as tables
from .models import *

class CPUTable(tables.Table):
    class Meta:
        model = CPU
        attrs = {"class": "table table-hover"}
        sequence = ("brand", "name")
        exclude = ("id", "cpu_world", "top_img", "bottom_img")

    name = tables.Column(linkify=True)

class RAMTable(tables.Table):
    class Meta:
        model = RAM
        attrs = {"class": "table table-hover"}
        exclude = ("id", )

class GPUTable(tables.Table):
    class Meta:
        model = GPU
        attrs = {"class": "table table-hover"}
        sequence = ("brand", "name", )
        exclude = ("id", "top_img", "bottom_img", "io_img")

    name = tables.Column(linkify=True)

class SoundCardTable(tables.Table):
    class Meta:
        model = SoundCard
        attrs = {"class": "table table-hover"}
        sequence = ("brand", "name", )
        exclude = ("id", "top_img", "bottom_img", "io_img")

    name = tables.Column(linkify=True)

class ExpansionCardTable(tables.Table):
    class Meta:
        model = ExpansionCard
        attrs = {"class": "table table-hover"}
        sequence = ("brand", "name", )
        exclude = ("id", "top_img", "bottom_img", "io_img")

    name = tables.Column(linkify=True)

class NICTable(tables.Table):
    class Meta:
        model = NIC
        attrs = {"class": "table table-hover"}
        exclude = ("id", "top_img", "bottom_img", "io_img")

    model = tables.Column(linkify=True)

class MotherboardTable(tables.Table):
    class Meta:
        model = Motherboard
        attrs = {"class": "table table-hover"}
        exclude = ("id", "top_img", "bottom_img", "io_img")

    model = tables.Column(linkify=True)

class PSUTable(tables.Table):
    class Meta:
        model = PSU
        attrs = {"class": "table table-hover"}
        exclude = ("id", "image")
    
    model = tables.Column(linkify=True)
    
class DriveTable(tables.Table):
    class Meta:
        model = Drive
        attrs = {"class": "table table-hover"}
        sequence = {"name"}
        exclude = {"id", "top_img", "bezel_img", "rear_img"}

    name = tables.Column(linkify=True)

class CaseTable(tables.Table):
    class Meta:
        model = Case
        attrs = {"class": "table table-hover"}
        exclude = ("id", "image_1", "image_2", "image_3" )

    model = tables.Column(linkify=True)

class MicroPropTable(tables.Table):
    class Meta:
        model = MicroProp
        attrs = {"class": "table table-hover"}
        exclude = {"id", "image_1", "image_2", "image_3", "image_4", "type"}
        sequence = {"name"}
    
    name = tables.Column(linkify=True)

class SBCTable(tables.Table):
    class Meta:
        model = SBC
        attrs = {"class": "table table-hover"}
        exclude = {"id", "usage"}
        sequence = {"type"}
    
    model = tables.Column(linkify=True)

class PeripheralTable(tables.Table):
    class Meta:
        model = Peripheral
        attrs = {"class": "table table-hover"}
        exclude = ("id", "brand", "model", "image_1", "image_2", "image_3")

    name = tables.Column(linkify=True)

class CableTable(tables.Table):
    class Meta:
        model = Cable
        attrs = {"class": "table table-hover"}
        sequence = {"name", "type"}
        exclude = ("id", "image_1", "image_2")
    
    name = tables.Column(linkify=True)