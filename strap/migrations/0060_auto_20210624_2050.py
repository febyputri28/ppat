# Generated by Django 3.1.7 on 2021-06-24 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0059_auto_20210624_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailclientdua',
            name='nik_kedua',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='strap.tempclientdua'),
        ),
    ]