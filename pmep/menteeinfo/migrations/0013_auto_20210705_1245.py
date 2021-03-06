# Generated by Django 3.2 on 2021-07-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menteeinfo', '0012_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='FMCG',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='analytics',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='consultancy',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='core',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='finance',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='no_of_mentees',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='other_mentorship',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='referral',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='software',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='suggestions',
        ),
        migrations.AddField(
            model_name='mentor',
            name='company',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='field',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='specialization',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='workprofile',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='degree',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='department',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='experience',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='graduation_year',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='rollno',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
