# Generated by Django 4.0.7 on 2022-11-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0022_cpu_cpu_world'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpu',
            name='component',
            field=models.IntegerField(default=0, verbose_name='Component Ports'),
        ),
        migrations.AddField(
            model_name='gpu',
            name='composite',
            field=models.IntegerField(default=0, verbose_name='Composite Ports'),
        ),
        migrations.AddField(
            model_name='gpu',
            name='svideo',
            field=models.IntegerField(default=0, verbose_name='S-Video Ports'),
        ),
    ]