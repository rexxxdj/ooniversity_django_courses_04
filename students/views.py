# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from forms import StudentModelForm
from django.contrib import messages
from django.template import RequestContext

def list_view(request):
    if request.GET:
        student = Student.objects.filter(courses__id=int(request.GET['course_id']))
    else:
        student = Student.objects.all()
    return render(request, 'students/list.html', {'students': student})

def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})

def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student= form.save()
            messages.success(request, u'Student %s %s has been successfully added.'%(student.name, student.surname))
            return redirect('students:list_view')
    else:
    	form = StudentModelForm()
    return render(request, 'students/add.html', {'form':form})

def edit(request,id):
    student_inst=Student.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST,instance=student_inst)
        if form.is_valid():
            student= form.save()
            messages.success(request, u'Info on the student has been sucessfully changed.')
            return redirect('students:list_view')                
    else:
        form = StudentModelForm(instance=student_inst)
    return render(request,"students/edit.html",{"form":form})    

def remove(request,id):
    student=Student.objects.get(pk=id)
    if request.method == 'POST':
        messages.success(request, u'Info on %s %s has been sucessfully deleted.'%(student.name, student.surname))
        student.delete()
        return redirect('students:list_view')
    return render(request,"students/remove.html",{"student":student})