from django.contrib import admin
from courses.models import Course, Lesson



class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,        {'fields': ['name', 'short_description']}),
        ('More info', {'fields': ['description']})
    ]


#, CourseAdmin
admin.site.register(Course, CourseAdmin)
'''
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
'''