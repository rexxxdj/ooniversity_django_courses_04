from django.contrib import admin
from courses.models import Course, Lesson


class Lessoninline(admin.TabularInline):
    fields = ('order', 'subject', 'description')
    model = Lesson
    extra = 2

class CourseAdmin(admin.ModelAdmin):    
    inlines = [Lessoninline]
    list_display = ('name', 'short_description')
    search_fields = ['name']



admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)