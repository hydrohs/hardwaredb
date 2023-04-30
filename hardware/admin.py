from django.contrib import admin
from django import forms

from .models import CPU, RAM, GPU, SoundCard, ExpansionCard, NIC, Motherboard, PSU, Drive, Case, System, MicroProp, Peripheral, Cable

admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(GPU)
admin.site.register(SoundCard)
admin.site.register(ExpansionCard)
admin.site.register(NIC)
admin.site.register(Motherboard)
admin.site.register(PSU)
admin.site.register(Drive)
admin.site.register(Case)
admin.site.register(Peripheral)
admin.site.register(Cable)
admin.site.register(MicroProp)

# Next 2 classes format RAM so that it's clear which id is being selected
# from admin panel, since there are many identically named RAM sticks
class RAMChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{} ({})".format(obj, obj.id)

@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name in ('ram1', 'ram2', 'ram3', 'ram4', 'ram5', 'ram6', 'ram7', 'ram8', 
        'ram9', 'ram10', 'ram11', 'ram12', 'ram13', 'ram14', 'ram15', 'ram16'):
            # Passing this list ignores the verbose_name from the System model, so adding a label restores it
            return RAMChoiceField(queryset=RAM.objects.all(), label='RAM', required=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)