#-*-coding: utf-8-*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm

def quadratic_results(request):
    context = {}
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            b = form.cleaned_data['b']
            a = form.cleaned_data['a']
            c = form.cleaned_data['c']

            d = b ** 2 - 4 * a * c

            if d < 0:
                result_message = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif d == 0:
                x = (-b + d**(1/2.0)) / 2*a
                result_message = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}" .format(x)
            else:
                x1 = (-b + d**(1/2.0)) / 2*a
                x2 = (-b - d**(1/2.0)) / 2*a
                result_message = "Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}" .format(x1, x2)

            context.update({'d': 'Дискриминант: %d' %d, 'result_message': result_message})
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
    return render(request, 'quadratic/results.html', {'form': form, 'context': context})
