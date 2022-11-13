from django.contrib import admin

from .models import CPU, RAM, GPU, SoundCard, ExpansionCard, NIC, Motherboard, PSU, Drive, Case, Peripheral, Cable

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