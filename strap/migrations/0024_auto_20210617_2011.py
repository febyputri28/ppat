# Generated by Django 3.1.7 on 2021-06-17 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0023_tempclientdua'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempclientsatu',
            name='nama_pertama',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='strap.clientsatu'),
        ),
    ]
