# Generated by Django 4.2.7 on 2023-12-02 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0089_peripheral'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cable',
            new_name='CableOld',
        ),
        migrations.DeleteModel(
            name='PeripheralOld',
        ),
    ]