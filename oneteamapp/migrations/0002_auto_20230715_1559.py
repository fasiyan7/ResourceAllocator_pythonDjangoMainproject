# Generated by Django 3.0.7 on 2023-07-15 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneteamapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('1', 'ADMIN'), ('2', 'STAFF'), ('3', 'VENDOR'), ('4', 'CUSTOMER')], default='1', max_length=200),
        ),
    ]
