# Generated by Django 3.1.7 on 2021-07-17 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0074_auto_20210713_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailclientdua',
            name='no_transaksi',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detailclientsatu',
            name='no_transaksi',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
