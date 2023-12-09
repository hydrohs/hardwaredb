from django.contrib import admin
from hardware.models import *

class ImageInline(admin.StackedInline):
    model = Image
    extra = 0

class CPUInline(admin.TabularInline):
    model = CPU
    fk_name = 'installed_in'
    classes = [ 'collapse', ]
    extra = 0

class RAMInline(admin.TabularInline):
    model = RAM
    fk_name = 'installed_in'
    classes = [ 'collapse', ]
    extra = 0

@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    fields = ( 'brand', 'model', 'name', 'speed', 'socket', 'cores', 'hyperthreading', 'cpu_world', 'notes', 'installed_in')

@admin.register(Cable)
class CableAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    fields = ( 'name', 'type', 'connectors_a', 'connectors_b', 'quantity', 'notes' )
    filter_horizontal = ['connectors_a', 'connectors_b', ]

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    fields = ( 'brand', 'model', 'name', 'mb_support', 'notes', 'installed_in' )

@admin.register(Drive)
class DriveAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    fields = ( 'brand', 'model', 'name', 'type', 'interface', 'capacity', 'internal', 'notes', 'installed_in' )

@admin.register(ExpansionCard)
class ExpansionCardAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    fields = ( 'brand', 'model', 'name', 'interface', 'io_panel', 'notes', 'installed_in' )

@admin.register(GPU)
class GPUAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    fields = ( 'brand', 'model', 'name', 'gpu_brand', 
              'interface', 'mda', 'cga', 'composite', 'vga', 
              'svideo', 'component', 'dvi', 'hdmi', 'minihdmi', 
              'microhdmi', 'dp', 'minidp', 'other', 'notes', 'installed_in' )

@admin.register(Micro)
class MicroPropAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    fields = ( 'brand', 'model', 'name', 'notes' )

@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    fields = ( 'brand', 'model', 'form_factor', 'socket', 
              'isa', 'isa16', 'vlb', 'pci', 'agp', 
              'pcie1', 'pcie4', 'pcie8', 'pcie16', 
              'ram', 'notes', 'installed_in' )

@admin.register(NIC)
class NICAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    fields = ( 'brand', 'model', 'wireless', 'speed', 'interface', 
              'aui', 'bnc', 'tp', 'notes', 'installed_in' )

@admin.register(PSU)
class PSUAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    fields = ( 'brand', 'model', 'wattage', 'spec', 'minus5v', 
              'molex', 'floppy', 'sata', 'cpu4pin', 'cpu8pin', 
              'pcie6pin', 'pcie8pin', 'notes', 'installed_in' )

@admin.register(Peripheral)
class PeripheralAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    fields = ( 'brand', 'model', 'name', 'type', 'ports', 'notes' )
    filter_horizontal = ['ports', ]

@admin.register(Proprietary)
class ProprietaryAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    fields = ( 'brand', 'model', 'name', 'os', 'notes' )

admin.site.register(RAM)

admin.site.register(SBC)

@admin.register(SoundCard)
class SoundCardAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    fields = ( 'brand', 'model', 'name', 'sb', 'interface', 'notes', 'installed_in')

@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    inlines = (CPUInline, RAMInline, ImageInline, )
    fields = [ 'name', 'os', 'notes', ]
    exclude = [ 'brand', 'model', ]

    def get_queryset(self, request):
        qs = super(SystemAdmin, self).get_queryset(request)
        return qs.filter(proprietary__isnull=True)