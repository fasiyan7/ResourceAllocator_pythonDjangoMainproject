# Generated by Django 3.0.7 on 2023-07-26 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneteamapp', '0035_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('assigntopic', models.FileField(upload_to='Assignment')),
                ('created', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
    ]