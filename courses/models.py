from django.db import models
# Create your models here.

class Course(models.Model):
    name = models.CharField(verbose_name=u"Name of Course", max_length=200)
    short_description = models.CharField(verbose_name=u"Short description", max_length=200) 
    description = models.TextField(verbose_name=u"Description") 

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=200) 
    description = models.TextField() 
    course = models.ForeignKey(Course) 
    order = models.IntegerField()

    def __unicode__(self):
    	return self.subject