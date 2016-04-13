from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal info', {
            'fields': ['name', 'surname', 'date_of_birth']
        }),
        ('Contact info', {
            'fields': ['email', 'phone', 'address', 'skype']
        }),
        ('Courses', {
            'fields': ['courses']}),
]


admin.site.register(Student, StudentAdmin)