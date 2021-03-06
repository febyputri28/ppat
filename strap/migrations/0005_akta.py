# Generated by Django 3.1.7 on 2021-05-24 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0004_karyawan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Akta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_urut', models.CharField(max_length=200)),
                ('nomor_akta', models.CharField(max_length=200)),
                ('tgl_akta', models.CharField(max_length=100)),
                ('jenis', models.CharField(blank=True, choices=[('AJB', 'AJB'), ('APHT', 'APHT'), ('SKMHT', 'SKMHT'), ('AH', 'AH'), ('APHB', 'APHB')], max_length=100, null=True)),
                ('client_pengalih', models.CharField(max_length=100)),
                ('client_penerima', models.CharField(max_length=200)),
                ('nomor_hak', models.CharField(max_length=200)),
                ('almt_aset', models.CharField(max_length=200)),
                ('luas_tanah', models.CharField(max_length=200)),
                ('luas_bgn', models.CharField(max_length=200)),
                ('harga_pengalihan', models.CharField(max_length=200)),
                ('nop', models.CharField(max_length=200)),
                ('njop', models.CharField(max_length=200)),
                ('tgl_ssp', models.CharField(max_length=200)),
                ('harga_ssp', models.CharField(max_length=200)),
                ('tgl_sbb', models.CharField(max_length=200)),
                ('harga_sbb', models.CharField(max_length=200)),
                ('keterangan', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Data Akta',
            },
        ),
    ]
