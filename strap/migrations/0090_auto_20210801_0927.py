# Generated by Django 3.1.7 on 2021-08-01 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0089_auto_20210728_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='karyawan',
            old_name='tanggal_karyawan',
            new_name='tanggal_lahir_karyawan',
        ),
    ]
