from django.contrib import admin

from ..admin_site import edc_protocol_register_admin
from ..models import ProtocolResponse


@admin.register(ProtocolResponse, site=edc_protocol_register_admin)
class ProtocolResponseAdmin(admin.ModelAdmin):
    list_display = ('protocol_request', 'status')
    list_filter = ['status']
