from django.contrib import admin
from django import forms

from .models import CPU, RAM, GPU, SoundCard, ExpansionCard, NIC, Motherboard, PSU, Drive, Case, System, MicroProp, SBC, Peripheral, Cable, Image, ImageAlbum

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
admin.site.register(SBC)
admin.site.register(ImageAlbum)

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
    
@admin.register(Image)    
class ImageAdmin(admin.ModelAdmin):
    # Formats image album names to be more clear as to which item they belong to
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "album":
            kwargs["queryset"] = ImageAlbum.objects.order_by('name')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    # This prevents adding albums from the image page, which crashes because the upload_to field
    # requires a model class, so they must be assigned to an object before uploading any images
    def get_form(self, request, obj=None, **kwargs):
        form = super(ImageAdmin, self).get_form(request, obj, **kwargs)
        field = form.base_fields["album"]
        field.widget.can_add_related = False
        field.widget.can_change_related = True
        field.widget.can_delete_related = True
        return form