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
    num_systems = System.objects.count() + MicroProp.objects.count()
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

    def get_context_data(self, **kwargs):
        context = super(GPUDetail, self).get_context_data(**kwargs)
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

class SoundCardDetail(DetailView):
    model = SoundCard

    def get_context_data(self, **kwargs):
        context = super(SoundCardDetail, self).get_context_data(**kwargs)
        context['interface'] = context['object'].get_interface_display()
        return context

class ExpansionCardList(SingleTableView):
    model = ExpansionCard
    table_class = ExpansionCardTable
    template_name = 'hardware/hardware_list.html'

class ExpansionCardDetail(DetailView):
    model = ExpansionCard
    template_name = 'hardware/expansion_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ExpansionCardDetail, self).get_context_data(**kwargs)
        context['interface'] = context['object'].get_interface_display()
        return context

class NICList(SingleTableView):
    model = NIC
    table_class = NICTable
    template_name = 'hardware/hardware_list.html'

class NICDetail(DetailView):
    model = NIC

    def get_context_data(self, **kwargs):
        context = super(NICDetail, self).get_context_data(**kwargs)
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

class MotherboardDetail(DetailView):
    model = Motherboard

    def get_context_data(self, **kwargs):
        context = super(MotherboardDetail, self).get_context_data(**kwargs)
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

class PSUDetail(DetailView):
    model = PSU

    def get_context_data(self, **kwargs):
        context = super(PSUDetail, self).get_context_data(**kwargs)
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

class DriveList(SingleTableView):
    model = Drive
    table_class = DriveTable
    template_name = 'hardware/hardware_list.html'

class DriveDetail(DetailView):
    model = Drive

    def get_context_data(self, **kwargs):
        context = super(DriveDetail, self).get_context_data(**kwargs)
        context['type'] = context['object'].get_type_display()
        context['interface'] = context['object'].get_interface_display()
        if context['object'].capacity:
            context['capacity'] = HumanReadable('size', context['object'].capacity, '')
        return context

class CaseList(SingleTableView):
    model = Case
    table_class = CaseTable
    template_name = 'hardware/hardware_list.html'

class CaseDetail(DetailView):
    model = Case

class SystemList(ListView):
    model = System
    context_object_name = 'systems'

class SystemDetail(DetailView):
    model = System

    def get_context_data(self, **kwargs):
        context = super(SystemDetail, self).get_context_data(**kwargs)
        # Gather all expansion card fields to pass only what is populated to context
        all_cards = (context['object'].expansion1,
        context['object'].expansion2,
        context['object'].expansion3,
        context['object'].expansion4,
        context['object'].expansion5,
        context['object'].expansion6
        )

        # Same as above but for drives
        all_drives = (context['object'].drive1,
        context['object'].drive2,
        context['object'].drive3,
        context['object'].drive4,
        context['object'].drive5,
        context['object'].drive6,
        context['object'].drive7,
        context['object'].drive8,
        context['object'].drive9,
        context['object'].drive10,
        context['object'].drive11,
        context['object'].drive12
        )

        # Again same, but for RAM
        all_ram = (context['object'].ram1,
        context['object'].ram2,
        context['object'].ram3,
        context['object'].ram4,
        context['object'].ram5,
        context['object'].ram6,
        context['object'].ram7,
        context['object'].ram8,
        context['object'].ram9,
        context['object'].ram10,
        context['object'].ram11,
        context['object'].ram12,
        context['object'].ram13,
        context['object'].ram14,
        context['object'].ram15,
        context['object'].ram16,
        )

        # Filters out null fields
        context['cards'] = []
        for card in all_cards:
            if card:
                context['cards'].append(card)

        # Same as above
        context['external_drives'] = []
        context['internal_drives'] = []
        for drive in all_drives:
            if drive:
                if drive.type in ('SSD', 'HDD'):
                    context['internal_drives'].append(drive)
                else:
                    context['external_drives'].append(drive)

        # Same again
        context['ram'] = []
        for ram in all_ram:
            if ram:
                context['ram'].append(ram)

        return context

class MicroList(SingleTableView):
    model = MicroProp
    
    template_name = 'hardware/hardware_list.html'

class MicroPropDetail(DetailView):
    model = MicroProp

    
class PeripheralList(SingleTableView):
    model = Peripheral
    table_class = PeripheralTable
    template_name = 'hardware/hardware_list.html'

class PeripheralDetail(DetailView):
    model = Peripheral

    def get_context_data(self, **kwargs):
        context = super(PeripheralDetail, self).get_context_data(**kwargs)
        context['type'] = context['object'].get_type_display()
        context['interface'] = context['object'].get_interface_display()
        return context


class CableList(SingleTableView):
    model = Cable
    table_class = CableTable
    template_name = 'hardware/hardware_list.html'

class CableDetail(DetailView):
    model = Cable

    def get_context_data(self, **kwargs):
        context = super(CableDetail, self).get_context_data(**kwargs)
        context['type'] = context['object'].get_type_display()
        return context