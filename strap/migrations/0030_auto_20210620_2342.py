# Generated by Django 3.1.7 on 2021-06-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0029_transaksiakta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempclientsatu',
            name='nik_pertama',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
