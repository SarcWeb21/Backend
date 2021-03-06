# Generated by Django 3.2 on 2021-06-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmpportal', '0003_remove_registration_degree_other'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='FMCG',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='analytics',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='consultancy',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='contact',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='core',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='degree',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='department',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='designation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='experience',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='finance',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='graduation_year',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='mail',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='no_of_mentees',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='other_mentorship',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='referral',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='rollno',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='software',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='suggestions',
            field=models.TextField(null=True),
        ),
    ]
