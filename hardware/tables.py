import django_tables2 as tables
from .models import *

class CPUTable(tables.Table):
    class Meta:
        model = CPU
        attrs = {"class": "table table-hover"}

    name = tables.Column(linkify=True)

class RAMTable(tables.Table):
    class Meta:
        model = RAM
        attrs = {"class": "table table-hover"}

class GPUTable(tables.Table):
    class Meta:
        model = GPU
        attrs = {"class": "table table-hover"}

class SoundCardTable(tables.Table):
    class Meta:
        model = SoundCard
        attrs = {"class": "table table-hover"}

class ExpansionCardTable(tables.Table):
    class Meta:
        model = ExpansionCard
        attrs = {"class": "table table-hover"}

class NICTable(tables.Table):
    class Meta:
        model = NIC
        attrs = {"class": "table table-hover"}

class MotherboardTable(tables.Table):
    class Meta:
        model = Motherboard
        attrs = {"class": "table table-hover"}

class CaseTable(tables.Table):
    class Meta:
        model = Case
        attrs = {"class": "table table-hover"}

class PSUTable(tables.Table):
    class Meta:
        model = PSU
        attrs = {"class": "table table-hover"}

class PeripheralTable(tables.Table):
    class Meta:
        model = Peripheral
        attrs = {"class": "table table-hover"}

class CableTable(tables.Table):
    class Meta:
        model = Cables
        attrs = {"class": "table table-hover"}