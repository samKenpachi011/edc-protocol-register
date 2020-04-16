from django.contrib import admin

from ..admin_site import edc_protocol_register_admin
from ..models import Protocol


@admin.register(Protocol, site=edc_protocol_register_admin)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = (
        'short_name', 'long_name', 'number',
        'approval_date')
    list_filter = ['approval_date']
