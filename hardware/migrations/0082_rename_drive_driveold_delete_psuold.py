# Generated by Django 4.2.7 on 2023-12-02 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0081_psu'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drive',
            new_name='DriveOld',
        ),
        migrations.DeleteModel(
            name='PSUOld',
        ),
    ]
