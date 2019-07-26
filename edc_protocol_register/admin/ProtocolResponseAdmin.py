from django.contrib import admin
from ..models import ProtocolResponse



class ProtocolResponseAdmin(admin.ModelAdmin):
    list_display = ('protocolrequest', 'status')
    list_filter = ['status']


admin.site.register(ProtocolResponse, ProtocolResponseAdmin)