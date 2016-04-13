from django.contrib import admin
from courses.models import Course, Lesson


class Lessoninline(admin.TabularInline):
    fields = ('order', 'subject', 'description')
    model = Lesson
    extra = 2

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,        {'fields': ['name', 'short_description']}),
        ('More info', {'fields': ['description'], 'classes': ['collapse']})
    ]
    inlines = [Lessoninline]
    list_display = ('name', 'short_description')


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)