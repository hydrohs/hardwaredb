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
        exclude = ("id", "top_img", "bottom_img", "io_img")

class ExpansionCardTable(tables.Table):
    class Meta:
        model = ExpansionCard
        attrs = {"class": "table table-hover"}
        exclude = ("id", "top_img", "bottom_img", "io_img")

class NICTable(tables.Table):
    class Meta:
        model = NIC
        attrs = {"class": "table table-hover"}
        exclude = ("id", "top_img", "bottom_img", "io_img")

class MotherboardTable(tables.Table):
    class Meta:
        model = Motherboard
        attrs = {"class": "table table-hover"}
        exclude = ("id", "top_img", "bottom_img", "io_img")

class CaseTable(tables.Table):
    class Meta:
        model = Case
        attrs = {"class": "table table-hover"}
        exclude = ("id", )

class PSUTable(tables.Table):
    class Meta:
        model = PSU
        attrs = {"class": "table table-hover"}
        exclude = ("id", "image")

class PeripheralTable(tables.Table):
    class Meta:
        model = Peripheral
        attrs = {"class": "table table-hover"}
        exclude = ("id", "image_1", "image_2", "image_3")

class CableTable(tables.Table):
    class Meta:
        model = Cables
        attrs = {"class": "table table-hover"}
        exclude = ("id", "image_1", "image_2")