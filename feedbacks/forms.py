# -*- coding: utf-8 -*-
from django import forms
from feedbacks.models import Feedback

class FeedbackForm(forms.ModelForm):    
	class Meta:
		model = Feedback
		fields = '__all__'


'''
class FeedbackForm(forms.ModelForm):    
	class Meta:
		model = Feedback
		widgets = {
			'name':forms.TextInput(attrs={'class':'form-control'}),
			'from_email':forms.TextInput(attrs={'class':'form-control'}),
			'subject':forms.TextInput(attrs={'class':'form-control'}),
			#'message':forms.TextInput(attrs={'class':'form-control'}),
		}
		message = forms.CharField(widget=forms.Textarea)
		fields = '__all__' 
'''		