# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.

class Course(models.Model):
    class Meta(object):
        verbose_name_plural = "Курсы"
    name = models.CharField(verbose_name=u"Name of Course", max_length=200)
    short_description = models.CharField(verbose_name=u"Short description", max_length=200) 
    description = models.TextField(verbose_name=u"Description") 

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Lesson(models.Model):
    class Meta(object):
        verbose_name = "Лекция"
        verbose_name_plural = "Лекции"
    subject = models.CharField(verbose_name = "Название", max_length=200) 
    description = models.TextField(verbose_name = "Описание") 
    course = models.ForeignKey(Course) 
    order = models.IntegerField(verbose_name = "№п.п")

    def __unicode__(self):
    	return self.subject