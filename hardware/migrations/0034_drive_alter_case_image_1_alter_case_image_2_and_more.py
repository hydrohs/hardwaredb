# Generated by Django 4.0.7 on 2022-11-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0033_alter_cable_interface_a_alter_cable_interface_b'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('FLOPPY5', '5.25" Floppy'), ('FLOPPY3', '3.5" Floppy'), ('ZIP', 'Zip'), ('CD', 'CD'), ('DVD', 'DVD'), ('BR', 'Bluray'), ('HDD', 'HDD'), ('SSD', 'SSD')], default='FLOPPY5', max_length=10)),
                ('interface', models.CharField(choices=[('FLOPPYEDGE', '34-Pin Floppy Edge'), ('FLOPPY', '34-Pin Floppy'), ('IDE', 'IDE'), ('SCSI', 'SCSI'), ('SATA', 'SATA'), ('M240', 'M.2 2240'), ('M280', 'M.2 2280')], default='FLOPPYEDGE', max_length=20)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('top_img', models.ImageField(blank=True, max_length=255, null=True, upload_to='drives')),
                ('bezel_img', models.ImageField(blank=True, max_length=255, null=True, upload_to='drives')),
                ('rear_img', models.ImageField(blank=True, max_length=255, null=True, upload_to='drives')),
            ],
        ),
        migrations.AlterField(
            model_name='case',
            name='image_1',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='case'),
        ),
        migrations.AlterField(
            model_name='case',
            name='image_2',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='cases'),
        ),
        migrations.AlterField(
            model_name='case',
            name='image_3',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='cases'),
        ),
    ]
