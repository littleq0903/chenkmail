from django.contrib import admin
from namelist.models import Professor, TA


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')

class TAAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')

admin.site.register(Professor, ProfessorAdmin)
admin.site.register(TA, TAAdmin)
