# Generated by Django 3.0.7 on 2023-07-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneteamapp', '0030_auto_20230724_1745'),
    ]

    operations = [
        
        migrations.RemoveField(
            model_name='batch',
            name='start_time',
        ),
        migrations.AddField(
            model_name='batch',
            name='endtime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='starttime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
