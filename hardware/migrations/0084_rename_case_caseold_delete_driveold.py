# Generated by Django 4.2.7 on 2023-12-02 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0083_drive'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Case',
            new_name='CaseOld',
        ),
        migrations.DeleteModel(
            name='DriveOld',
        ),
    ]