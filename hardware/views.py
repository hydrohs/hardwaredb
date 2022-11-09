from django.shortcuts import render
from django.views.generic import DetailView
from django_tables2 import SingleTableView
from .models import *
from .tables import *

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

class CPUList(SingleTableView):
    model = CPU
    table_class = CPUTable
    template_name = 'hardware/hardware_list.html'

class RAMList(SingleTableView):
    model = RAM
    table_class = RAMTable
    template_name = 'hardware/hardware_list.html'

class GPUList(SingleTableView):
    model = GPU
    table_class = GPUTable
    template_name = 'hardware/hardware_list.html'

class SoundCardList(SingleTableView):
    model = SoundCard
    table_class = SoundCardTable
    template_name = 'hardware/hardware_list.html'

class ExpansionCardList(SingleTableView):
    model = ExpansionCard
    table_class = ExpansionCardTable
    template_name = 'hardware/hardware_list.html'

class NICList(SingleTableView):
    model = NIC
    table_class = NICTable
    template_name = 'hardware/hardware_list.html'

class MotherboardList(SingleTableView):
    model = Motherboard
    table_class = MotherboardTable
    template_name = 'hardware/hardware_list.html'

class CaseList(SingleTableView):
    model = Case
    table_class = CaseTable
    template_name = 'hardware/hardware_list.html'

class PeripheralList(SingleTableView):
    model = Peripheral
    table_class = PeripheralTable
    template_name = 'hardware/hardware_list.html'

class PSUList(SingleTableView):
    model = PSU
    table_class = PSUTable
    template_name = 'hardware/hardware_list.html'

class CableList(SingleTableView):
    model = Cables
    table_class = CableTable
    template_name = 'hardware/hardware_list.html'