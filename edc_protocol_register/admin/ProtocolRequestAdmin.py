from django.contrib import admin
from ..models import ProtocolResponse, ProtocolRequest,Protocol
from django.db.models import F

class ProtocolResponseInline(admin.TabularInline):
    model = ProtocolResponse


class ProtocolRequestAdmin(admin.ModelAdmin):
    inlines = [ProtocolResponseInline]
    list_display = ('name', 'snippet', 'pi_email', 'request_date')
    list_filter = ['request_date']
    search_fields = ['name']


admin.site.register(ProtocolRequest, ProtocolRequestAdmin)