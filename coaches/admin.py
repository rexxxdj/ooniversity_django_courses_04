from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
    list_display = ('usname', 'gender', 'skype', 'description')
    #list_filter = ['user__is_stuff']



admin.site.register(Coach, CoachAdmin)