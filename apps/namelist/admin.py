from django.contrib import admin
from namelist.models import Sendor, Receiver


class SendorAdmin(admin.ModelAdmin):
    pass

class ReceiverAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sendor, SendorAdmin)
admin.site.register(Receiver, ReceiverAdmin)
