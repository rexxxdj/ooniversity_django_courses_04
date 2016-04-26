from coaches.models import Coach
from courses.models import Course
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View


class MixinCoachContext(object):
	
	def get_context_data(self, **kwargs):
		var = kwargs
		context = super(MixinCoachContext, self).get_context_data(**kwargs)
		context['coach'] = Coach.objects.get(id=var['coach_id'])
		context['teacher'] = Course.objects.filter(coach=var['coach_id'])
		context['assistant'] = Course.objects.filter(assistant=var['coach_id'])
		return context


class CoachDetailView(MixinCoachContext, TemplateView):
	template_name = 'coaches/detail.html' 


#def detail(request, coach_id):
#    coach = Coach.objects.get(id=coach_id)
#    teacher = Course.objeects.filter(coach=coach_id)
#    assistant = Course.objects.filter(assistant=coach_id)
#    return render(request, 'coaches/detail.html', {'coach': coach,  'teacher': teacher, 'assistant': assistant})
