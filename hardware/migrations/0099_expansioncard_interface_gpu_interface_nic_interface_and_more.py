# Generated by Django 4.2.7 on 2023-12-02 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0098_slots_remove_expansioncard_interface_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expansioncard',
            name='interface',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hardware.slots'),
        ),
        migrations.AddField(
            model_name='gpu',
            name='interface',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hardware.slots'),
        ),
        migrations.AddField(
            model_name='nic',
            name='interface',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hardware.slots'),
        ),
        migrations.AddField(
            model_name='soundcard',
            name='interface',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hardware.slots'),
        ),
    ]