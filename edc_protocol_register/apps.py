from django.apps import AppConfig as DjangoAppConfig
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from edc_device.constants import CENTRAL_SERVER
#from .models import Protocol,ProtocolResponse,ProtocolRequest



class AppConfig(DjangoAppConfig):
    name = 'edc_protocol_register'

    def ready(self):
        from .models import Protocol
        from .models import ProtocolResponse
        from .models import ProtocolRequest


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Protocol Register'
    institution = 'Botswana-Harvard AIDS Institute'


class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
    device_role = CENTRAL_SERVER
    device_id = '99'
