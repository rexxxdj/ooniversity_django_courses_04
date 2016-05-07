# -*- coding: utf-8 -*-
from django import forms
from courses.models import Course,Lesson

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
       # widgets = {
		#	'name':forms.TextInput(attrs={'class':'form-control'}),
			#'short_description':forms.TextInput(attrs={'class':'form-control'}),
			#'description':forms.TextInput(attrs={'class':'form-control'}),
			#'message':forms.TextInput(attrs={'class':'form-control'}),
	#	}

class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'