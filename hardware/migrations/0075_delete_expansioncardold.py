# Generated by Django 4.2.7 on 2023-12-02 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0074_expansioncard'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExpansionCardOld',
        ),
    ]