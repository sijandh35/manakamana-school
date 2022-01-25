from django.contrib import admin
from .models import *
from django_extensions.admin import ForeignKeyAutocompleteAdmin


class ScheduleAdmin(ForeignKeyAutocompleteAdmin):
    # User is your FK attribute in your model
    # first_name and email are attributes to search for in the FK model
    related_search_fields = {
       'period': ('name', 'time'),
    }

    # fields = ('period', 'grade', 'day', 'subject')
    fields = ('period', 'grade', 'day', 'subject')
# Register your models here.

admin.site.register(HeadersFooters)
admin.site.register(HomePage)
admin.site.register(Events)
admin.site.register(Teachers)
admin.site.register(Schedule)
admin.site.register(Message)
admin.site.register(Period)
