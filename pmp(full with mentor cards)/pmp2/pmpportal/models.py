from django.db import models

# Create your models here.
class Registration(models.Model):
    id=models.AutoField(primary_key=True)
    full_name=models.CharField( max_length=255, null=True)
    rollno=models.CharField(max_length=9, null=True)
    department=models.CharField( max_length=255, null=True)
    degree=models.CharField( max_length=255, null=True)
    # degree_other=models.CharField( max_length=255)
    graduation_year=models.CharField( max_length=10, null=True)
    designation=models.CharField( max_length=255, null=True)
    experience=models.TextField(null=True)
    contact=models.CharField( max_length=12, null=True)
    mail=models.CharField( max_length=255, null=True)
    # field_mentorship=models.CharField(max_length=255)
    no_of_mentees=models.CharField(max_length=255, null=True)
    referral=models.CharField(max_length=255, null=True)
    suggestions=models.TextField(null=True)
    analytics=models.CharField(max_length=50, null=True)
    consultancy=models.CharField(max_length=50, null=True)
    finance=models.CharField(max_length=50, null=True)
    FMCG=models.CharField(max_length=50, null=True)
    software=models.CharField(max_length=50, null=True)
    core=models.CharField(max_length=100, null=True)
    other_mentorship=models.CharField(max_length=100, null=True)