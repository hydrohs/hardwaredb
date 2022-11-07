# Generated by Django 4.0.7 on 2022-11-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0017_alter_cables_interface_a_alter_cables_interface_b_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peripheral',
            name='type',
            field=models.CharField(choices=[('M', 'Mouse'), ('KB', 'Keyboard'), ('ZIP', 'Zip Drive'), ('GAME', 'Gamepad'), ('JOY', 'Joystick'), ('MIDI', 'Midi'), ('SPK', 'Speakers'), ('LCD', 'LCD'), ('CRT', 'CRT'), ('OTHER', 'Other')], default='M', max_length=10),
        ),
    ]