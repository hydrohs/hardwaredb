# Generated by Django 3.2.7 on 2021-10-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('speed', models.IntegerField()),
                ('socket', models.CharField(max_length=200)),
                ('cores', models.IntegerField()),
                ('hyperthreading', models.BooleanField()),
                ('notes', models.TextField()),
                ('top_img', models.ImageField(max_length=255, upload_to='cpus')),
                ('bottom_img', models.ImageField(max_length=255, upload_to='cpus')),
            ],
        ),
    ]
