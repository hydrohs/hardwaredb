# Generated by Django 4.0.7 on 2022-11-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0030_alter_peripheral_interface_alter_peripheral_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='image_1',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='peripherals'),
        ),
        migrations.AddField(
            model_name='case',
            name='image_2',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='peripherals'),
        ),
        migrations.AddField(
            model_name='case',
            name='image_3',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='perihperals'),
        ),
    ]
