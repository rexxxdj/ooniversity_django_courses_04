# -*- coding: utf-8 -*-
from courses.models import Course, Lesson
from forms import CourseModelForm, LessonModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import View


class CourseDetailView(DetailView):
    model = Course
    context_object_name = "course"
    template_name = "courses/detail.html"    

    def get_context_data(self,**kwargs):
        context = super(CourseDetailView,self).get_context_data(**kwargs)
        context["title"] = "Course detail"
        pk = self.kwargs['pk']
        context["lessons"] = Lesson.objects.filter(course_id = pk)
        return context


class CourseCreateView(CreateView):
    model = Course
    context_object_name = "course"
    template_name = "courses/add.html"
    success_url = reverse_lazy('index')    

    def get_context_data(self,**kwargs):
        context = super(CourseCreateView,self).get_context_data(**kwargs)
        context["title"] = "Course creation"
        return context
    
    def form_valid(self,form):
        course = form.save()
        messages.success(self.request, u'Course %s has been successfully added.'%(course.name))
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course   
    context_object_name = "course"
    template_name = "courses/edit.html"    
    class_form = CourseModelForm

    def get_context_data(self,**kwargs):
        context = super(CourseUpdateView,self).get_context_data(**kwargs)
        context["pk"] = self.kwargs['pk']
        context["title"] = "Course update"        
        return context
    
    def form_valid(self,form):
        curs = form.save()
        messages.success(self.request, u'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('courses:edit', kwargs={'pk': pk})


class CourseDeleteView(DeleteView):
    model = Course
    template_name = "courses/remove.html" 
    success_url = reverse_lazy('index')

    def get_context_data(self,**kwargs):
        context = super(CourseDeleteView,self).get_context_data(**kwargs)
        context["title"] = "Course deletion"
        return context
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, u'Course %s has been deleted.'%self.get_object().name)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)



class LessonCreateView(View):
    form_class = LessonModelForm
    template_name = "courses/add_lesson.html"

    def get(self, request, *args, **kwargs):
        course=Course.objects.get(pk=kwargs['course_id'])
        form = LessonModelForm(initial = {'course': course})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            lesson= form.save()
            messages.success(request, u'Lesson %s has been successfully added.'%(lesson.subject))
            return redirect('courses:detail', lesson.course.id)

        return render(request, self.template_name, {'form': form})

        
#def add_lesson(request,id):
#    if request.method == 'POST':
#        form = LessonModelForm(request.POST)
#        if form.is_valid():
#            lesson= form.save()
#            messages.success(request, u'Lesson %s has been successfully added.'%(lesson.subject))
#            return redirect('courses:detail', lesson.course.id)
#    else:
#    	 course=Course.objects.get(pk=id)
#        form = LessonModelForm(initial = {'course': course})
#    return render(request, 'courses/add_lesson.html', {'form':form})    
