# Generated by Django 3.0.7 on 2023-07-20 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('oneteamapp', '0010_usermodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
