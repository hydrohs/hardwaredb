import django_tables2 as tables
from .models import *

class CPUTable(tables.Table):
    class Meta:
        model = CPU
        attrs = {"class": "table table-hover"}
        fields = ( 'brand', 'name', 'model', 'speed', 'socket', 'cores',
                  'hyperthreading', 'notes', 'installed_in' )

    name = tables.Column(linkify=True)

class RAMTable(tables.Table):
    class Meta:
        model = RAM
        attrs = {"class": "table table-hover"}
        fields = ( 'type', 'interface', 'size', 'speed', 'ecc', 'installed_in' )

class GPUTable(tables.Table):
    class Meta:
        model = GPU
        attrs = {"class": "table table-hover"}
        fields = ( 'brand', 'name', 'model', 'interface', 
                  'gpu_brand', 'ports', 'notes', 'installed_in')

    name = tables.Column(linkify=True)

class SoundCardTable(tables.Table):
    class Meta:
        model = SoundCard
        attrs = {"class": "table table-hover"}
        fields = ( 'brand', 'name', 'model', 'sb', 'interface', 
                  'notes', 'installed_in' )

    name = tables.Column(linkify=True)

class ExpansionCardTable(tables.Table):
    class Meta:
        model = ExpansionCard
        attrs = {"class": "table table-hover"}
        fields = ( 'brand', 'model', 'name', 'interface', 'io_panel', 
                  'notes', 'installed_in' )
    model = tables.Column(linkify=True)

class NICTable(tables.Table):
    class Meta:
        model = NIC
        attrs = {"class": "table table-hover"}
        fields = ( 'brand', 'model', 'wireless', 'speed', 'interface', 
                  'ports', 'installed_in' )

    model = tables.Column(linkify=True)

class MotherboardTable(tables.Table):
    class Meta:
        model = Motherboard
        attrs = {"class": "table table-hover"}
        fields = ( 'brand', 'model', 'form_factor', 'socket', 'slots', 
                  'ram', 'notes', 'installed_in' )

    model = tables.Column(linkify=True)

class PSUTable(tables.Table):
    class Meta:
        model = PSU
        attrs = {"class": "table table-hover"}
        fields = ( 'brand', 'model', 'wattage', 'spec', 'minus5v', 
                  'connectors', 'notes', 'installed_in' )
    
    model = tables.Column(linkify=True)
    
class DriveTable(tables.Table):
    human_readable_capacity = tables.Column(verbose_name='Capacity')
    class Meta:
        model = Drive
        attrs = {"class": "table table-hover"}
        fields = ( 'name', 'brand', 'model', 'type', 'interface', 
                  'human_readable_capacity', 'internal', 'notes', 'installed_in' )

    name = tables.Column(linkify=True)

class CaseTable(tables.Table):
    all_mb_support = tables.Column(verbose_name='Motherboard Compatibility')
    class Meta:
        model = Case
        attrs = {"class": "table table-hover"}
        fields = ( 'brand', 'model', 'all_mb_support', 'notes', 'installed_in' )

    model = tables.Column(linkify=True)

class MicroTable(tables.Table):
    class Meta:
        model = Micro
        attrs = {"class": "table table-hover"}
        fields = ( 'brand', 'name', 'model', 'notes' )
    
    name = tables.Column(linkify=True)

class ProprietaryTable(tables.Table):
    class Meta:
        model = Proprietary
        attrs = {"class": "table table-hover"}
        fields = ( 'brand', 'name', 'model', 'os', 'notes' )
    
    name = tables.Column(linkify=True)

class SBCTable(tables.Table):
    class Meta:
        model = SBC
        attrs = {"class": "table table-hover"}
        fields = ( 'type', 'model', 'quantity' )
    
    model = tables.Column(linkify=True)

class PeripheralTable(tables.Table):
    all_ports = tables.Column(verbose_name='Ports')
    class Meta:
        model = Peripheral
        attrs = {"class": "table table-hover"}
        fields = ( 'name', 'type', 'all_ports', 'notes')

    name = tables.Column(linkify=True)

class CableTable(tables.Table):
    all_connectors_a = tables.Column(verbose_name='Connectors (A Side)')
    all_connectors_b = tables.Column(verbose_name='Connectors (B Side)')

    class Meta:
        model = Cable
        attrs = {"class": "table table-hover"}
        fields = ( 'name', 'type', 'all_connectors_a', 'all_connectors_b', 'quantity', 'notes')
    
    name = tables.Column(linkify=True)