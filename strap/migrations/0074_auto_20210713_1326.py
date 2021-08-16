# Generated by Django 3.1.7 on 2021-07-13 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0073_karyawan_id_karyawan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempkaryawan',
            name='almt_karyawan',
        ),
        migrations.RemoveField(
            model_name='tempkaryawan',
            name='desa_karyawan',
        ),
        migrations.RemoveField(
            model_name='tempkaryawan',
            name='kab_karyawan',
        ),
        migrations.RemoveField(
            model_name='tempkaryawan',
            name='kec_karyawan',
        ),
        migrations.RemoveField(
            model_name='tempkaryawan',
            name='nama_karyawan',
        ),
        migrations.RemoveField(
            model_name='tempkaryawan',
            name='nik_karyawan',
        ),
        migrations.RemoveField(
            model_name='tempkaryawan',
            name='prov_karyawan',
        ),
        migrations.RemoveField(
            model_name='tempkaryawan',
            name='rt_karyawan',
        ),
        migrations.RemoveField(
            model_name='tempkaryawan',
            name='rw_karyawan',
        ),
        migrations.RemoveField(
            model_name='tempkaryawan',
            name='status_kewarganegaraan_karyawan',
        ),
        migrations.RemoveField(
            model_name='tempkaryawan',
            name='tanggal_karyawan',
        ),
        migrations.RemoveField(
            model_name='tempkaryawan',
            name='tempat_lahir_karyawan',
        ),
        migrations.RemoveField(
            model_name='tempkaryawan',
            name='user',
        ),
        migrations.AddField(
            model_name='tempkaryawan',
            name='id_karyawan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='strap.karyawan'),
        ),
    ]
