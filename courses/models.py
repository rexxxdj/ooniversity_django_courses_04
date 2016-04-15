# -*- coding: utf-8 -*-
from django.db import models
from coaches.models import Coach
# Create your models here.

class Course(models.Model):
    class Meta:
        verbose_name_plural = "Курсы"

    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200) 
    description = models.TextField() 
    coach = models.ForeignKey(Coach, null=True, related_name="coach_courses")
    assistant = models.ForeignKey(Coach, null=True, related_name="assistant_courses")

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Lesson(models.Model):
    class Meta:
        verbose_name_plural = "Уроки"
    subject = models.CharField(max_length=200) 
    description = models.TextField() 
    course = models.ForeignKey(Course) 
    order = models.PositiveIntegerField()

    def __unicode__(self):
    	return self.subject