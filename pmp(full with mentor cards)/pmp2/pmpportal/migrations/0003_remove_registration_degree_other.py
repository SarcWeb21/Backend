# Generated by Django 3.2 on 2021-06-16 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmpportal', '0002_registration_degree_other'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='degree_other',
        ),
    ]
