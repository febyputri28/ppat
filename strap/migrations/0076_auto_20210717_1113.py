# Generated by Django 3.1.7 on 2021-07-17 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0075_auto_20210717_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akta',
            name='no_transaksi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='strap.detailclientsatu'),
        ),
    ]
