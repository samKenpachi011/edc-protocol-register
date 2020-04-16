from django.contrib import admin

from ..admin_site import edc_protocol_register_admin
from ..models import ProtocolRequest, ProtocolResponse


class ProtocolResponseInline(admin.TabularInline):
    model = ProtocolResponse


@admin.register(ProtocolRequest, site=edc_protocol_register_admin)
class ProtocolRequestAdmin(admin.ModelAdmin):
    inlines = [ProtocolResponseInline]
    list_display = (
        'short_name', 'long_name', 'description',
        'email', 'snippet', 'pi_email',
        'duration')
    list_filter = ['request_date']
    search_fields = ['name']
