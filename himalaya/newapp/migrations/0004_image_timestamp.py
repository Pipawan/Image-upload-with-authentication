# Generated by Django 4.2.7 on 2023-11-24 17:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_ipaddress_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
