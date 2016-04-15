# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coach(models.Model):
    class Meta:
        verbose_name_plural = "Инструкторы"
    
    GENDER_CHOICES = (
    	(u"M", u"Male"),
    	(u"F", u"Female"),
    	)
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=35)
    description = models.TextField() 

    def __unicode__(self):              # __unicode__ on Python 2
        return self.user.get_username()

    def usname(self):              # __unicode__ on Python 2
        return self.user.get_full_name()