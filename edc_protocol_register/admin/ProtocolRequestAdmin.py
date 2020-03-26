from django.contrib import admin
from ..models import ProtocolResponse, ProtocolRequest

class ProtocolResponseInline(admin.TabularInline):
    model = ProtocolResponse


class ProtocolRequestAdmin(admin.ModelAdmin):
    inlines = [ProtocolResponseInline]
    list_display = (
        'short_name', 'long_name', 'description',
        'email', 'snippet', 'pi_email', 'request_date',
        'duration')
    list_filter = ['request_date']
    search_fields = ['name']


admin.site.register(ProtocolRequest, ProtocolRequestAdmin)