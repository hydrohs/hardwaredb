# Generated by Django 4.0.7 on 2022-11-13 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0031_case_image_1_case_image_2_case_image_3'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cables',
            new_name='Cable',
        ),
    ]
