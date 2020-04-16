from django.db.models.signals import post_save
from django.dispatch import receiver

from .protocol_request import ProtocolRequest
from .protocol_response import ProtocolResponse
from ..approve_protocol import ApproveProtocol


@receiver(post_save, weak=False, sender=ProtocolRequest,
          dispatch_uid='protocol_request_on_post_save')
def protocol_request_on_post_save(sender, instance, raw, created, **kwargs):
    """Creates a protocol response.
    """
    if not raw:
        try:
            ProtocolResponse.objects.get(protocol_request=instance)
        except ProtocolResponse.DoesNotExist:
            ProtocolResponse.objects.create(
                protocol_request=instance)


@receiver(post_save, weak=False, sender=ProtocolResponse,
          dispatch_uid='protocol_response_on_post_save')
def protocol_response_on_post_save(sender, instance, raw, created, **kwargs):
    """Creates a protocol.
    """
    if not raw:
        approve_protocol = ApproveProtocol()
        print(" I am here *******8")
        if instance.status == 'A':
            print("Now inside @@@@@@@@@@@")
            approve_protocol.approve(protocol_response=instance)
        elif instance.status == 'R':
            approve_protocol.reject(protocol_response=instance)