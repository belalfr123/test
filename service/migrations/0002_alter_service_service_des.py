# Generated by Django 4.2.1 on 2023-05-26 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_des',
            field=models.ImageField(upload_to=''),
        ),
    ]
