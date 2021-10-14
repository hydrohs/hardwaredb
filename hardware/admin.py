from django.contrib import admin

from .models import CPU, RAM, GPU, SoundCard, ExpansionCard, NIC, Motherboard, Case, Peripheral, PSU

admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(GPU)
admin.site.register(SoundCard)
admin.site.register(ExpansionCard)
admin.site.register(Motherboard)
admin.site.register(NIC)
admin.site.register(Case)
admin.site.register(PSU)
admin.site.register(Peripheral)