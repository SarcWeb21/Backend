# Generated by Django 3.2 on 2021-07-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menteeinfo', '0015_alter_mentor_hits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='experience',
            field=models.TextField(max_length=350, null=True),
        ),
    ]