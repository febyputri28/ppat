# Generated by Django 3.1.7 on 2021-08-09 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strap', '0091_akta_nib'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempakta',
            name='nib',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
