from django.shortcuts import render
from students.models import Student

def list_view(request):
    if request.GET:
        student = Student.objects.filter(courses__id=int(request.GET['course_id']))
    else:
        student = Student.objects.all()
    return render(request, 'students/list.html', {'students': student})

def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})