# Generated by Django 4.2.7 on 2023-12-02 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0066_delete_cpuold'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GPU',
            new_name='GPUOld',
        ),
    ]