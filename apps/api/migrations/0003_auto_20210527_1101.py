# Generated by Django 2.2.10 on 2021-05-27 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_equipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='cedula',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='personal',
            name='correo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personal',
            name='telefono',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]