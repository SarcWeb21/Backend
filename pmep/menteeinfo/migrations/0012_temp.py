# Generated by Django 3.2 on 2021-07-05 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menteeinfo', '0011_auto_20210705_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference_1', models.CharField(max_length=10)),
                ('preference_2', models.CharField(max_length=10)),
                ('preference_3', models.CharField(max_length=10)),
                ('preference_4', models.CharField(max_length=10)),
                ('preference_5', models.CharField(max_length=10)),
            ],
        ),
    ]
