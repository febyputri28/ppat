# Generated by Django 3.1.7 on 2021-07-10 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0067_auto_20210710_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tempkaryawan',
            old_name='id_karyawan',
            new_name='nomor_pengenal',
        ),
    ]
