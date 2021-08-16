# Generated by Django 3.1.7 on 2021-06-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0037_remove_akta_almt_aset'),
    ]

    operations = [
        migrations.AddField(
            model_name='akta',
            name='jabatan_pt',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='jenis_bukti_perjanjian',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='jenis_kuasa',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='jumlah_perjanjian',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='keterangan_kuasa',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='no_perjanjian',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='pt',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='tanggal_perjanjian',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]