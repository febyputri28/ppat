# Generated by Django 3.1.7 on 2021-06-21 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0036_auto_20210621_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='akta',
            name='almt_aset',
        ),
    ]