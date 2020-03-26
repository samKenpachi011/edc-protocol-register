from django.contrib import admin
from ..models import Protocol



class ProtocolAdmin(admin.ModelAdmin):
    list_display = (
        'short_name', 'long_name', 'number',
        'approval_date')
    list_filter = ['approval_date']

admin.site.register(Protocol,ProtocolAdmin)