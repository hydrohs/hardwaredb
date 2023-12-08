import django_tables2 as tables
from .models import *

class CPUTable(tables.Table):
    class Meta:
        model = CPU
        attrs = {"class": "table table-hover"}
        sequence = ("brand", "name")
        exclude = ("id", "cpu_world", "polymorphic_ctype", "hardware_ptr", )

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
        sequence = ("brand", "name", "model", "interface", )
        exclude = ("id", "polymorphic_ctype", "hardware_ptr", )

    name = tables.Column(linkify=True)

class SoundCardTable(tables.Table):
    class Meta:
        model = SoundCard
        attrs = {"class": "table table-hover"}
        sequence = ("brand", "name", )
        exclude = ("id", "polymorphic_ctype", "hardware_ptr", )

    name = tables.Column(linkify=True)

class ExpansionCardTable(tables.Table):
    class Meta:
        model = ExpansionCard
        attrs = {"class": "table table-hover"}
        sequence = ("brand", "model", "name", )
        exclude = ("id", "polymorphic_ctype", "hardware_ptr", )

    model = tables.Column(linkify=True)

class NICTable(tables.Table):
    class Meta:
        model = NIC
        attrs = {"class": "table table-hover"}
        exclude = ("id", "name", "polymorphic_ctype", "hardware_ptr", )

    model = tables.Column(linkify=True)

class MotherboardTable(tables.Table):
    class Meta:
        model = Motherboard
        attrs = {"class": "table table-hover"}
        exclude = ("id", "name", "polymorphic_ctype", "hardware_ptr", )

    model = tables.Column(linkify=True)

class PSUTable(tables.Table):
    class Meta:
        model = PSU
        attrs = {"class": "table table-hover"}
        exclude = ("id", "name", "polymorphic_ctype", "hardware_ptr", )
    
    model = tables.Column(linkify=True)
    
class DriveTable(tables.Table):
    class Meta:
        model = Drive
        attrs = {"class": "table table-hover"}
        sequence = ("name", )
        exclude = ("id", "polymorphic_ctype", "hardware_ptr", )

    name = tables.Column(linkify=True)

class CaseTable(tables.Table):
    class Meta:
        model = Case
        attrs = {"class": "table table-hover"}
        exclude = ("id", "name", "polymorphic_ctype", "hardware_ptr", )

    model = tables.Column(linkify=True)

class MicroTable(tables.Table):
    class Meta:
        model = Micro
        attrs = {"class": "table table-hover"}
        exclude = ("id", "polymorphic_ctype", "hardware_ptr", "type")
        sequence = ("brand", "name", )
    
    name = tables.Column(linkify=True)

class ProprietaryTable(tables.Table):
    class Meta:
        model = Proprietary
        attrs = {"class": "table table-hover"}
        exclude = ("id", "polymorphic_ctype", "hardware_ptr", "type")
        sequence = ("brand", "name", )
    
    name = tables.Column(linkify=True)

class SBCTable(tables.Table):
    class Meta:
        model = SBC
        attrs = {"class": "table table-hover"}
        exclude = ("id", "usage", )
        sequence = ("type", )
    
    model = tables.Column(linkify=True)

class PeripheralTable(tables.Table):
    class Meta:
        model = Peripheral
        attrs = {"class": "table table-hover"}
        exclude = ("id", "brand", "model", "polymorphic_ctype", "hardware_ptr", )

    name = tables.Column(linkify=True)

class CableTable(tables.Table):
    class Meta:
        model = Cable
        attrs = {"class": "table table-hover"}
        exclude = ("id", "brand", "model", "polymorphic_ctype", "hardware_ptr", )
        sequence = ("name", "type", "quantity", )
    
    name = tables.Column(linkify=True)