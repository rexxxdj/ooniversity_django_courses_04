# -*- coding: utf-8 -*-
from django import forms

class QuadraticForm(forms.Form):

    a = forms.FloatField(label="коэффициент а")
    b = forms.FloatField(label="коэффициент b")
    c = forms.FloatField(label="коэффициент c")