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
    num_cables = Cable.objects.count()
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

class GPUDetailView(DetailView):
    model = GPU

    def get_context_data(self, **kwargs):
        context = super(GPUDetailView, self).get_context_data(**kwargs)
        context['interface'] = context['object'].get_interface_display()

        port_type = {'MDA': context['object'].mda,
        'CGA': context['object'].cga,
        'Composite': context['object'].composite,
        'VGA': context['object'].vga,
        'S-Video': context['object'].svideo,
        'Component': context['object'].component,
        'DVI': context['object'].dvi,
        'HDMI': context['object'].hdmi,
        'Mini HDMI': context['object'].minihdmi,
        'Micro HDMI': context['object'].microhdmi,
        'DisplayPort': context['object'].dp,
        'Mini DisplayPort': context['object'].minidp}

        ports = []
        for key, value in port_type.items():
            if value != 0:
                ports.append('{} ({})'.format(key, value))

        context['ports'] = ', '.join(ports)
        return context

class SoundCardList(SingleTableView):
    model = SoundCard
    table_class = SoundCardTable
    template_name = 'hardware/hardware_list.html'

class SoundCardDetailView(DetailView):
    model = SoundCard

    def get_context_data(self, **kwargs):
        context = super(SoundCardDetailView, self).get_context_data(**kwargs)
        context['interface'] = context['object'].get_interface_display()
        return context

class ExpansionCardList(SingleTableView):
    model = ExpansionCard
    table_class = ExpansionCardTable
    template_name = 'hardware/hardware_list.html'

class ExpansionCardDetailView(DetailView):
    model = ExpansionCard
    template_name = 'hardware/expansion_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ExpansionCardDetailView, self).get_context_data(**kwargs)
        context['interface'] = context['object'].get_interface_display()
        return context

class NICList(SingleTableView):
    model = NIC
    table_class = NICTable
    template_name = 'hardware/hardware_list.html'

class NICDetailView(DetailView):
    model = NIC

    def get_context_data(self, **kwargs):
        context = super(NICDetailView, self).get_context_data(**kwargs)
        context['interface'] = context['object'].get_interface_display()
        port_type = {'AUI': context['object'].aui,
        'BNC': context['object'].bnc,
        'Ethernet': context['object'].tp}

        ports = []
        for key, value in port_type.items():
            if value != 0:
                ports.append('{} ({})'.format(key, value))

        context['ports'] = ', '.join(ports)

        context['speed'] = context['object'].get_speed_display()
        context['ports'] = ', '.join(ports)
        return context

class MotherboardList(SingleTableView):
    model = Motherboard
    table_class = MotherboardTable
    template_name = 'hardware/hardware_list.html'

class MotherboardDetailView(DetailView):
    model = Motherboard

    def get_context_data(self, **kwargs):
        context = super(MotherboardDetailView, self).get_context_data(**kwargs)
        context['form_factor'] = context['object'].get_form_factor_display()
        slot_type = {'8-Bit ISA': context['object'].isa,
        '16-Bit ISA': context['object'].isa16,
        'VLB': context['object'].vlb,
        'PCI': context['object'].pci,
        'AGP': context['object'].agp,
        'PCIe x1': context['object'].pcie1,
        'PCIe x4': context['object'].pcie4,
        'PCIe x8': context['object'].pcie8,
        'PCIe x16': context['object'].pcie16}

        slots = []
        for key, value in slot_type.items():
            if value != 0:
                slots.append('{} ({})'.format(key, value))

        context['slots'] = ', '.join(slots)
        return context

class PSUList(SingleTableView):
    model = PSU
    table_class = PSUTable
    template_name = 'hardware/hardware_list.html'

class PSUDetailView(DetailView):
    model = PSU

    def get_context_data(self, **kwargs):
        context = super(PSUDetailView, self).get_context_data(**kwargs)
        connector_type = {'Molex': context['object'].molex,
        'Floppy': context['object'].floppy,
        'SATA': context['object'].sata,
        '4-Pin CPU': context['object'].cpu4pin,
        '8-Pin CPU': context['object'].cpu8pin,
        '6-Pin PEG': context['object'].pcie6pin,
        '8-Pin PEG': context['object'].pcie8pin}

        connectors = []
        for key, value in connector_type.items():
            if value != 0:
                connectors.append('{} ({})'.format(key, value))

        context['spec'] = context['object'].get_spec_display()
        context['connectors'] = ', '.join(connectors)
        return context

class CaseList(SingleTableView):
    model = Case
    table_class = CaseTable
    template_name = 'hardware/hardware_list.html'

class CaseDetailView(DetailView):
    model = Case

class PeripheralList(SingleTableView):
    model = Peripheral
    table_class = PeripheralTable
    template_name = 'hardware/hardware_list.html'

class PeripheralDetailView(DetailView):
    model = Peripheral

    def get_context_data(self, **kwargs):
        context = super(PeripheralDetailView, self).get_context_data(**kwargs)
        context['type'] = context['object'].get_type_display()
        context['interface'] = context['object'].get_interface_display()
        return context


class CableList(SingleTableView):
    model = Cable
    table_class = CableTable
    template_name = 'hardware/hardware_list.html'

class CableDetailView(DetailView):
    model = Cable

    def get_context_data(self, **kwargs):
        context = super(CableDetailView, self).get_context_data(**kwargs)
        context['type'] = context['object'].get_type_display()
        return context