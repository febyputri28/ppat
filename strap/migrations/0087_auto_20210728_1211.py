# Generated by Django 3.1.7 on 2021-07-28 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0086_akta_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailclientsatu',
            name='nik_pertama',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
