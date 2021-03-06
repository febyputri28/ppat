# Generated by Django 3.1.7 on 2021-06-22 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0053_auto_20210622_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akta',
            name='harga_pengalihan',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='harga_sbb',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='harga_ssp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='luas_bgn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='luas_tanah',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nik_saksi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='njop',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='no_perjanjian',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nomor_akta',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='nop',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='rt_saksi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='rw_saksi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='tanggal_perjanjian',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='tgl_akta',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='tgl_sbb',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='akta',
            name='tgl_ssp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
