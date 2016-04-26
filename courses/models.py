# -*- coding: utf-8 -*-
from django.db import models
from coaches.models import Coach
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200) 
    description = models.TextField() 
    coach = models.ForeignKey(Coach, null=True, blank=True, related_name="coach_courses")
    assistant = models.ForeignKey(Coach, null=True, blank=True, related_name="assistant_courses")

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=200) 
    description = models.TextField() 
    course = models.ForeignKey(Course) 
    order = models.PositiveIntegerField()

    def __unicode__(self):
    	return self.subject

    def get_absolute_url(self):
        return reverse_lazy("courses:detail", self.pk)