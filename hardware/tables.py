import django_tables2 as tables
from .models import *

class CPUTable(tables.Table):
    class Meta:
        model = CPU
    name = tables.Column(linkify=True)

class RAMTable(tables.Table):
    class Meta:
        model = RAM

class GPUTable(tables.Table):
    class Meta:
        model = GPU

class SoundCardTable(tables.Table):
    class Meta:
        model = SoundCard

class ExpansionCardTable(tables.Table):
    class Meta:
        model = ExpansionCard

class NICTable(tables.Table):
    class Meta:
        model = NIC

class MotherboardTable(tables.Table):
    class Meta:
        model = Motherboard

class CaseTable(tables.Table):
    class Meta:
        model = Case

class PSUTable(tables.Table):
    class Meta:
        model = PSU

class PeripheralTable(tables.Table):
    class Meta:
        model = Peripheral

class CableTable(tables.Table):
    class Meta:
        model = Cables