# Generated by Django 3.1.7 on 2021-05-07 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karyawan',
            name='jenkel_karyawan',
            field=models.CharField(blank=True, choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=100, null=True),
        ),
    ]
