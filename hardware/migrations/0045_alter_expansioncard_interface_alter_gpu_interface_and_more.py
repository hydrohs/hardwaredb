# Generated by Django 4.0.7 on 2022-11-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0044_case_notes_system_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expansioncard',
            name='interface',
            field=models.CharField(choices=[('ISA', '8-bit ISA'), ('ISA16', '16-bit ISA'), ('VLB', 'VLB'), ('PCI', 'PCI'), ('PCMCIA', 'PCMCIA'), ('AGP', 'AGP'), ('AGP2', 'AGP 2x'), ('AGP4', 'AGP 4x'), ('AGP8', 'AGP 8x'), ('PCIE1', 'PCIe x1'), ('PCIE4', 'PCIe x4'), ('PCIE8', 'PCIe x8'), ('PCIE16', 'PCIe x16'), ('M2', 'M.2 2230')], default='ISA', max_length=10),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='interface',
            field=models.CharField(choices=[('ISA', '8-bit ISA'), ('ISA16', '16-bit ISA'), ('VLB', 'VLB'), ('PCI', 'PCI'), ('PCMCIA', 'PCMCIA'), ('AGP', 'AGP'), ('AGP2', 'AGP 2x'), ('AGP4', 'AGP 4x'), ('AGP8', 'AGP 8x'), ('PCIE1', 'PCIe x1'), ('PCIE4', 'PCIe x4'), ('PCIE8', 'PCIe x8'), ('PCIE16', 'PCIe x16'), ('M2', 'M.2 2230')], default='ISA', max_length=10),
        ),
        migrations.AlterField(
            model_name='nic',
            name='interface',
            field=models.CharField(choices=[('ISA', '8-bit ISA'), ('ISA16', '16-bit ISA'), ('VLB', 'VLB'), ('PCI', 'PCI'), ('PCMCIA', 'PCMCIA'), ('AGP', 'AGP'), ('AGP2', 'AGP 2x'), ('AGP4', 'AGP 4x'), ('AGP8', 'AGP 8x'), ('PCIE1', 'PCIe x1'), ('PCIE4', 'PCIe x4'), ('PCIE8', 'PCIe x8'), ('PCIE16', 'PCIe x16'), ('M2', 'M.2 2230')], default='ISA', max_length=6),
        ),
        migrations.AlterField(
            model_name='soundcard',
            name='interface',
            field=models.CharField(choices=[('ISA', '8-bit ISA'), ('ISA16', '16-bit ISA'), ('VLB', 'VLB'), ('PCI', 'PCI'), ('PCMCIA', 'PCMCIA'), ('AGP', 'AGP'), ('AGP2', 'AGP 2x'), ('AGP4', 'AGP 4x'), ('AGP8', 'AGP 8x'), ('PCIE1', 'PCIe x1'), ('PCIE4', 'PCIe x4'), ('PCIE8', 'PCIe x8'), ('PCIE16', 'PCIe x16'), ('M2', 'M.2 2230')], default='ISA', max_length=10),
        ),
    ]
