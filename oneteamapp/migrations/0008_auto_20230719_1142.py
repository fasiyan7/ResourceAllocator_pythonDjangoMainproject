# Generated by Django 3.0.7 on 2023-07-19 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneteamapp', '0007_auto_20230719_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='check_password',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=140),
        ),
    ]
