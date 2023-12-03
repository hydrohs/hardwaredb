# Generated by Django 4.2.7 on 2023-12-03 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0116_ram_installed_in_alter_system_os'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='installed_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case', to='hardware.system'),
        ),
        migrations.AddField(
            model_name='drive',
            name='installed_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drives', to='hardware.system'),
        ),
        migrations.AddField(
            model_name='expansioncard',
            name='installed_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expansioncards', to='hardware.system'),
        ),
        migrations.AddField(
            model_name='gpu',
            name='installed_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gpus', to='hardware.system'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='installed_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='motherboard', to='hardware.system'),
        ),
        migrations.AddField(
            model_name='nic',
            name='installed_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nics', to='hardware.system'),
        ),
        migrations.AddField(
            model_name='psu',
            name='installed_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='psu', to='hardware.system'),
        ),
        migrations.AddField(
            model_name='soundcard',
            name='installed_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='soundcards', to='hardware.system'),
        ),
    ]
