from django.contrib import admin
from .models import *
from django.forms.models import BaseInlineFormSet

admin.site.register(RAM)
admin.site.register(SBC)
admin.site.register(FormFactor)
admin.site.register(Slot)
admin.site.register(DriveInterface)
admin.site.register(Port)
admin.site.register(PeripheralType)
admin.site.register(CableType)

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

@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    inlines = (CPUInline, RAMInline, ImageInline, )
    fields = [ 'name', 'os', 'notes', ]
    exclude = [ 'brand', 'model', ]

@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )

@admin.register(GPU)
class GPUAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )

@admin.register(SoundCard)
class SoundCardAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )

@admin.register(ExpansionCard)
class ExpansionCardAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )

@admin.register(NIC)
class NICAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )

@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )

@admin.register(PSU)
class PSUAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )

@admin.register(Drive)
class DriveAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )

@admin.register(Peripheral)
class PeripheralAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    filter_horizontal = ['ports', ]

@admin.register(Cable)
class CableAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    exclude = [ 'brand', 'model', ]
    filter_horizontal = ['connectors_a', 'connectors_b', ]

@admin.register(MicroProp)
class MicroPropAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )