from django.db import models
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200) 
    description = models.TextField() 

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=200) 
    description = models.TextField() 
    course = models.ForeignKey(Course) 
    order = models.IntegerField()

    def __unicode__(self):
    	return self.subject