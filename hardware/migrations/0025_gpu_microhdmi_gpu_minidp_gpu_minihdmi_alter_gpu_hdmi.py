# Generated by Django 4.0.7 on 2022-11-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0024_rename_pice1_motherboard_pcie1'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpu',
            name='microhdmi',
            field=models.IntegerField(default=0, verbose_name='Micro HDMI Ports'),
        ),
        migrations.AddField(
            model_name='gpu',
            name='minidp',
            field=models.IntegerField(default=0, verbose_name='Mini DisplayPort Ports'),
        ),
        migrations.AddField(
            model_name='gpu',
            name='minihdmi',
            field=models.IntegerField(default=0, verbose_name='Mini HDMI Ports'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='hdmi',
            field=models.IntegerField(default=0, verbose_name='HDMI Ports'),
        ),
    ]
