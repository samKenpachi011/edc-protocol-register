from django.apps import AppConfig as DjangoAppConfig
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from edc_device.constants import CENTRAL_SERVER
#from .models import protocol,protocol_response,protocol_request


class AppConfig(DjangoAppConfig):
    name = 'edc_protocol_register'
    verbose_name = "EDC Protocol Register"
    admin_site_name = 'edc_protocol_register_admin'

    def ready(self):
        from .models import protocol_request_on_post_save
        from .models import protocol_response_on_post_save


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'protocol Register'
    institution = 'Botswana-Harvard AIDS Institute'


class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
    device_role = CENTRAL_SERVER
    device_id = '99'
