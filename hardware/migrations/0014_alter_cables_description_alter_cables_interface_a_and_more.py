# Generated by Django 4.0.7 on 2022-10-31 11:45

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0013_rename_interface_cables_interface_a_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cables',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='cables',
            name='interface_a',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('SERIAL', 'Serial'), ('PARALLEL', 'Parallel'), ('GAME', 'Gameport'), ('MIDI', 'Midi'), ('ADB', 'ADB'), ('SCSI', 'SCSI'), ('PS2', 'PS/2'), ('USB', 'USB'), ('PIN', 'PIN Connector'), ('OTHER', 'Other')], default='OTHER', max_length=52, verbose_name='Interface A'),
        ),
        migrations.AlterField(
            model_name='cables',
            name='interface_b',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('SERIAL', 'Serial'), ('PARALLEL', 'Parallel'), ('GAME', 'Gameport'), ('MIDI', 'Midi'), ('ADB', 'ADB'), ('SCSI', 'SCSI'), ('PS2', 'PS/2'), ('USB', 'USB'), ('PIN', 'PIN Connector'), ('OTHER', 'Other')], default='OTHER', max_length=52, verbose_name='Interface B'),
        ),
    ]
