from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django_tables2 import SingleTableView
from .models import *
from .tables import *

def index(requet):
    # Count number of objects for all classes
    num_cpus = CPU.objects.count()
    num_ram = RAM.objects.count()
    num_gpus = GPU.objects.count()
    num_sound = SoundCard.objects.count()
    num_exp = ExpansionCard.objects.count()
    num_nics = NIC.objects.count()
    num_mbs = Motherboard.objects.count()
    num_psus = PSU.objects.count()
    num_drives = Drive.objects.count()
    num_cases = Case.objects.count()
    num_systems = System.objects.count() + Proprietary.objects.count() + Micro.objects.count()
    num_periphs = Peripheral.objects.count()
    num_cables = Cable.objects.count()

    context = {
        'num_cpus': num_cpus,
        'num_ram': num_ram,
        'num_gpus': num_gpus,
        'num_sound': num_sound,
        'num_exp': num_exp,
        'num_nics': num_nics,
        'num_mbs': num_mbs,
        'num_psus': num_psus,
        'num_drives': num_drives,
        'num_cases': num_cases,
        'num_systems': num_systems,
        'num_periphs': num_periphs,
        'num_cables': num_cables,
    }

    return render(requet, 'hardware/index.html', context=context)

class CPUDetail(DetailView):
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

class GPUDetail(DetailView):
    model = GPU

class SoundCardList(SingleTableView):
    model = SoundCard
    table_class = SoundCardTable
    template_name = 'hardware/hardware_list.html'

class SoundCardDetail(DetailView):
    model = SoundCard

class ExpansionCardList(SingleTableView):
    model = ExpansionCard
    table_class = ExpansionCardTable
    template_name = 'hardware/hardware_list.html'

class ExpansionCardDetail(DetailView):
    model = ExpansionCard
    template_name = 'hardware/expansion_detail.html'

class NICList(SingleTableView):
    model = NIC
    table_class = NICTable
    template_name = 'hardware/hardware_list.html'

class NICDetail(DetailView):
    model = NIC

class MotherboardList(SingleTableView):
    model = Motherboard
    table_class = MotherboardTable
    template_name = 'hardware/hardware_list.html'

class MotherboardDetail(DetailView):
    model = Motherboard

class PSUList(SingleTableView):
    model = PSU
    table_class = PSUTable
    template_name = 'hardware/hardware_list.html'

class PSUDetail(DetailView):
    model = PSU

class DriveList(SingleTableView):
    model = Drive
    table_class = DriveTable
    template_name = 'hardware/hardware_list.html'

class DriveDetail(DetailView):
    model = Drive

class CaseList(SingleTableView):
    model = Case
    table_class = CaseTable
    template_name = 'hardware/hardware_list.html'

class CaseDetail(DetailView):
    model = Case

class SystemList(ListView):
    model = System
    queryset = System.objects.filter(proprietary__isnull=True)
    context_object_name = 'systems'

class SystemDetail(DetailView):
    model = System

class MicroList(SingleTableView):
    model = Micro
    table_class = MicroTable
    template_name = 'hardware/hardware_list.html'

class MicroDetail(DetailView):
    model = Micro

class ProprietaryList(SingleTableView):
    model = Proprietary
    table_class = ProprietaryTable
    template_name = 'hardware/hardware_list.html'

class ProprietaryDetail(DetailView):
    model = Proprietary

class SBCList(SingleTableView):
    model = SBC
    table_class = SBCTable
    template_name = 'hardware/hardware_list.html'

class SBCDetail(DetailView):
    model = SBC
    
class PeripheralList(SingleTableView):
    model = Peripheral
    table_class = PeripheralTable
    template_name = 'hardware/hardware_list.html'

class PeripheralDetail(DetailView):
    model = Peripheral

class CableList(SingleTableView):
    model = Cable
    table_class = CableTable
    template_name = 'hardware/hardware_list.html'

class CableDetail(DetailView):
    model = Cable