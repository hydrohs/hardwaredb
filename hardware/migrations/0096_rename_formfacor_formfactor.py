# Generated by Django 4.2.7 on 2023-12-02 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0095_formfacor_remove_case_mb_support_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FormFacor',
            new_name='FormFactor',
        ),
    ]
