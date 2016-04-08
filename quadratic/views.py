# -*- coding: utf-8 -*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm

def quadratic_results(request):
    text = {'error': False}
    for name_value in ['a', 'b', 'c']:
        valid = Validation(name_value, request.GET.get(name_value, ''))
        if valid.valid_quadratic():
            text[name_value] = valid.value_int
        else:
            text['error'] = True
            text[name_value + '_error'] = valid.error_msg
            text[name_value] = valid.value
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            d = b ** 2 - 4 * a * c
            if d < 0:
                result = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif d == 0:
                result = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %0.1f" % (-b / 2 * a)
            else:
                x1 = (-b + d ** (1/2.0)) / (2 * a)
                x2 = (-b - d ** (1/2.0)) / (2 * a)
                result = "Квадратное уравнение имеет два действительных корня: x1 = %0.1f, x2 = %0.1f" % (x1, x2)
            text.update(dict(d=str(int(d)), result=str(result)))
    else:
        form = QuadraticForm()
    text.update({ 'form' : form })
    return render(request, "results.html",  text )

class Validation(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.value_int = None
        self.error_msg = None

    def valid_quadratic(self):
        if not self.value:
            self.error_msg = 'коэффициент не определен'
            return False
        try:
            self.value_int = int(self.value)
        except ValueError:
            self.error_msg = 'коэффициент не целое число'
            return False

        if self.name == 'a' and self.value_int == 0:
            self.error_msg = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
            return False
        return True