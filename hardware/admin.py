from django.contrib import admin

from .models import Image, FormFactor, CPU, RAM, GPU, SoundCard, ExpansionCard, NIC, Motherboard, PSU, Drive, Case, MicroProp, SBC, Peripheral, Cable

admin.site.register(RAM)
admin.site.register(SBC)
admin.site.register(FormFactor)

class ImageInline(admin.StackedInline):
    model = Image
    extra = 0

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

@admin.register(Cable)
class CableAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )
    exclude = [ 'brand', 'model', ]

@admin.register(MicroProp)
class MicroPropAdmin(admin.ModelAdmin):
    inlines = (ImageInline, )