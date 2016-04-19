# -*- coding: utf-8 -*-
from django import forms

class QuadraticForm(forms.Form):

    a = forms.FloatField(label="коэффициент а")
    b = forms.FloatField(label="коэффициент b")
    c = forms.FloatField(label="коэффициент c")

    def clean_a(self):
        clean = self.cleaned_data['a']
        if clean == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return self.cleaned_data['a']