# Generated by Django 3.2.4 on 2021-07-04 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menteeinfo', '0007_alter_mentor_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='gray_out',
            field=models.CharField(default=1, max_length=1000),
        ),
        migrations.AddField(
            model_name='mentor',
            name='hits',
            field=models.IntegerField(default=0, max_length=1000),
        ),
    ]
