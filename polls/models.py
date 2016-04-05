from django.db import models

# Create your models here.
class Student(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=35)
	surname = models.CharField(max_length=35)
	patronymic = models.CharField(max_length=35)
	rating = models.IntegerField()
	package = models.CharField(max_length=35)
	birth_date = models.DateField()
	address = models.CharField(max_length=255)
	email = models.EmailField()
	skype = models.CharField(max_length=35)