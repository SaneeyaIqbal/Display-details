# Generated by Django 3.0 on 2019-12-04 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=35)),
                ('lastName', models.CharField(blank=True, max_length=35)),
                ('skills', models.CharField(max_length=40)),
            ],
        ),
    ]
