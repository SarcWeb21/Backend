# Generated by Django 3.2 on 2021-07-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menteeinfo', '0017_alter_mentor_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='gray_out',
            field=models.CharField(default=1, max_length=1000),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='hits',
            field=models.IntegerField(default=0),
        ),
    ]