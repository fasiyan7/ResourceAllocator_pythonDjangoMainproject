# Generated by Django 3.0.7 on 2023-07-24 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneteamapp', '0031_auto_20230724_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='endtime',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='starttime',
        ),
    ]
