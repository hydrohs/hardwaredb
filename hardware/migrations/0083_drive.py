# Generated by Django 4.2.7 on 2023-12-02 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0082_rename_drive_driveold_delete_psuold'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('hardware_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hardware.hardware')),
                ('type', models.CharField(choices=[('FLOPPY5', '5.25" Floppy'), ('FLOPPY3', '3.5" Floppy'), ('ZIP', 'Zip'), ('CD', 'CD'), ('DVD', 'DVD'), ('BR', 'Bluray'), ('HDD', 'HDD'), ('SSD', 'SSD')], default='FLOPPY5', max_length=10)),
                ('interface', models.CharField(choices=[('FLOPPYEDGE', '34-Pin Floppy Edge'), ('FLOPPY', '34-Pin Floppy'), ('APPLE', 'Apple 20-Pin'), ('IDE', 'IDE'), ('SCSI', 'SCSI'), ('SATA', 'SATA'), ('M240', 'M.2 2240'), ('M280', 'M.2 2280')], default='FLOPPYEDGE', max_length=20)),
                ('capacity', models.IntegerField(blank=True, null=True, verbose_name='Capacity (MB)')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('hardware.hardware',),
        ),
    ]
