from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *

def index(requet):
    # Count number of objects for all classes
    num_cpu = CPU.objects.count()
    num_ram = RAM.objects.count()
    num_gpu = GPU.objects.count()
    num_cables = Cables.objects.count()
    num_sound = SoundCard.objects.count()
    num_exp = ExpansionCard.objects.count()
    num_nic = NIC.objects.count()
    num_mb = Motherboard.objects.count()
    num_case = Case.objects.count()
    num_periph = Peripheral.objects.count()
    num_psu = PSU.objects.count()

    context = {
        'num_cpu': num_cpu,
        'num_ram': num_ram,
        'num_gpu': num_gpu,
        'num_cables': num_cables,
        'num_sound': num_sound,
        'num_exp': num_exp,
        'num_nic': num_nic,
        'num_mb': num_mb,
        'num_case': num_case,
        'num_periph': num_periph,
        'num_psu': num_psu,
    }

    return render(requet, 'hardware/index.html', context=context)

class CPUDetailView(DetailView):
    model = CPU

    def get_context_data(self, **kwargs):
        context = super(CPUDetailView, self).get_context_data(**kwargs)
        context['cpu_speed'] = HumanReadable('cpu', context['object'].speed, '')
        return context

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

class CableList(ListView):
    model = Cables
    template_name = 'hardware/hardware_list.html'