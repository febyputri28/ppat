# Generated by Django 3.1.7 on 2021-07-22 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0078_auto_20210717_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='akta',
            name='bulan',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='tahun',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='tanggal',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tempakta',
            name='bulan',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tempakta',
            name='tahun',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tempakta',
            name='tanggal',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
