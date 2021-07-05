from django.db import models

# Create your models here.
class Mentee(models.Model):
	# id = models.AutoField(primary_key = True)
	full_name = models.CharField(max_length = 255, null=True)
	roll_no = models.CharField(max_length = 9, null=True)
	department = models.CharField(max_length = 255, null=True)
	graduation_year = models.CharField(max_length = 10, null=True)
	contact_number = models.CharField(max_length = 12, null=True)
	email_id = models.CharField(max_length = 255, null=True)
	preference_1 = models.CharField(max_length = 10)
	preference_2 = models.CharField(max_length = 10)
	preference_3 = models.CharField(max_length = 10)
	preference_4 = models.CharField(max_length = 10)
	preference_5 = models.CharField(max_length = 10)
	SOP = models.TextField(default = '')
    
#mentor data
class Mentor(models.Model):
    rollno=models.CharField(max_length=9, null=True)
    department=models.CharField( max_length=255, null=True)
    degree=models.CharField( max_length=255, null=True)
    graduation_year=models.CharField( max_length=10, null=True)
    workprofile=models.CharField( max_length=255, null=True)
    company=models.CharField( max_length=255, null=True)
    experience=models.CharField(max_length=350, null=True)
    field = models.CharField(max_length=10, null=True)
    specialization = models.CharField(max_length= 100, null=True)
    hits = models.IntegerField(default = 0, null=True)
    gray_out = models.CharField(max_length = 1000, default = 1, null=True)

#temp to check preferences
class temp(models.Model):
    preference_1 = models.CharField(max_length = 10)
    preference_2 = models.CharField(max_length = 10)
    preference_3 = models.CharField(max_length = 10)
    preference_4 = models.CharField(max_length = 10)
    preference_5 = models.CharField(max_length = 10)
