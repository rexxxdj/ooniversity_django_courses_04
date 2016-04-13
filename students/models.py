# -*- coding: utf-8 -*- 
from django.db import models
from courses.models import Course

# Create your models here.
class Student(models.Model):	
	class Meta(object):
		verbose_name_plural = "Студенты"
			
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	address = models.CharField(max_length=255)
	skype = models.CharField(max_length=35)
	courses = models.ManyToManyField(Course)

	def __unicode__(self):
		return  self.name+ " " +self.surname