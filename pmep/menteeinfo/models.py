from django.db import models

# Create your models here.
class Mentee(models.Model):
	id = models.AutoField(primary_key = True)
	full_name = models.CharField(max_length = 255)
	roll_no = models.CharField(max_length = 9)
	department = models.CharField(max_length = 255)
	graduation_year = models.CharField(max_length = 10)
	contact_number = models.CharField(max_length = 12)
	email_id = models.CharField(max_length = 255)
	preference_1 = models.CharField(max_length = 10)
	preference_2 = models.CharField(max_length = 10)
	preference_3 = models.CharField(max_length = 10)
