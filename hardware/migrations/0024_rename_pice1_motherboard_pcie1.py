# Generated by Django 4.0.7 on 2022-11-11 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0023_gpu_component_gpu_composite_gpu_svideo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motherboard',
            old_name='pice1',
            new_name='pcie1',
        ),
    ]