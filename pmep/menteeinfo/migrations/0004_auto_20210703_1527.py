# Generated by Django 3.2.4 on 2021-07-03 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menteeinfo', '0003_mentor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='mentor',
            table='Mentors',
        ),
    ]
