# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):
    """
    Input variables of the quadratic equation
    """
    a = forms.FloatField(label='Введите коэффициент a ', 
    					widget=forms.TextInput(attrs={'size': '10'}))
    b = forms.FloatField(label='Введите коэффициент b ', 
    					widget=forms.TextInput(attrs={'size': '10'}))
    c = forms.FloatField(label='Введите коэффициент c ', 
    					widget=forms.TextInput(attrs={'size': '10'}))