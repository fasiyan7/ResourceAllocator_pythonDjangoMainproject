# Generated by Django 3.0.7 on 2023-07-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneteamapp', '0020_auto_20230723_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfernceHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lapname', models.CharField(max_length=200)),
            ],
        ),
    ]