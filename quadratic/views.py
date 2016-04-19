# -*- coding: utf-8 -*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    text = {'error': False}
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['a']
            c = form.cleaned_data['a']
            d = b**2 - 4*a*c
            if d < 0:
                result = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif d == 0:
                x = (-b + d**(1/2.0)) / 2*a
                result = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}.".format(x)
            else:
                x1 = (-b + d**(1/2.0)) / 2*a
                x2 = (-b - d**(1/2.0)) / 2*a
                result = "Дискриминант равен нулю, квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}.".format(x1, x2)
            text.update({'d':d, 'result': result})
        else:
            text['error'] = True
    else:
        form = QuadraticForm()

    text['form'] = form
    return render(request, 'results.html', text)
