from django.shortcuts import render
from django.views.generic import ListView

from .models import CPU, RAM, GPU, SoundCard, ExpansionCard, NIC, Motherboard, Case, Peripheral, PSU

def index(request):
    return render(request, 'hardware/index.html')

class CPUList(ListView):
    model = CPU
    template_name = 'hardware/hardware_list.html'

class RAMList(ListView):
    model = RAM
    template_name = 'hardware/hardware_list.html'

class GPUList(ListView):
    model = GPU
    template_name = 'hardware/hardware_list.html'

class SoundCardList(ListView):
    model = SoundCard
    template_name = 'hardware/hardware_list.html'

class ExpansionCardList(ListView):
    model = ExpansionCard
    template_name = 'hardware/hardware_list.html'

class NICList(ListView):
    model = NIC
    template_name = 'hardware/hardware_list.html'

class MotherboardList(ListView):
    model = Motherboard
    template_name = 'hardware/hardware_list.html'

class CaseList(ListView):
    model = Case
    template_name = 'hardware/hardware_list.html'

class PeripheralList(ListView):
    model = Peripheral
    template_name = 'hardware/hardware_list.html'

class PSUList(ListView):
    model = PSU
    template_name = 'hardware/hardware_list.html'