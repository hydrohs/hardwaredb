# Generated by Django 4.2.7 on 2023-12-02 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0102_peripheraltype_port_alter_driveinterface_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='peripheral',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hardware.peripheraltype'),
        ),
    ]