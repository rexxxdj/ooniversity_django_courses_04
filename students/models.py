# -*- coding: utf-8 -*- 
from django.db import models
from courses.models import Course

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=35)
	surname = models.CharField(max_length=35)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	address = models.CharField(max_length=255)
	skype = models.CharField(max_length=35)
	courses = models.ManyToManyField(Course)

	def Full_name(self):
		return  self.name+ " " +self.surname