# Generated by Django 3.2.4 on 2021-07-04 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menteeinfo', '0008_auto_20210704_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='hits',
            field=models.IntegerField(default=0),
        ),
    ]