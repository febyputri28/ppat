# Generated by Django 3.1.7 on 2021-06-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0013_auto_20210612_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='akta',
            name='alamat_kedua',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='desa_kedua',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='kab_kedua',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='kec_kedua',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='nama_kedua',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='nik_kedua',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='pekerjaan_kedua',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='prov_kedua',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='rt_kedua',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='rw_kedua',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='status_kewarganegaraan_kedua',
            field=models.CharField(blank=True, choices=[('Warga Negara Indonesia', 'Warga Negara Indonesia'), ('Warga Negara Asing', 'Warga Negara Asing')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='tanggal_lahir_kedua',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='akta',
            name='tempat_lahir_kedua',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
