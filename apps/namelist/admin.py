from django.contrib import admin
from namelist.models import Professor, TA


class ProfessorAdmin(admin.ModelAdmin):
    pass

class TAAdmin(admin.ModelAdmin):
    pass

admin.site.register(Professor, ProfessorAdmin)
admin.site.register(TA, TAAdmin)
