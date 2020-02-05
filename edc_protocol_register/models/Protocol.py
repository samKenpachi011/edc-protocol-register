from django.db import models
from .ProtocolResponse import ProtocolResponse
from .import ProtocolRequest
from django.db.models.signals import post_save
from ..email import send_email
from ..validators import *


class Protocol(models.Model):

    short_name = models.CharField(
        verbose_name="Protocol short name",
        max_length=50,
        null=False,
        blank=False
    )

    long_name = models.CharField(
        verbose_name="Protocol long name",
        max_length=250,
        null=False,
        blank=False
    )

    number = models.IntegerField(
        verbose_name="assigned protocol number",
        null=False,
        blank=True,
        validators=[validate_protocol_number]
    )

    approval_date = models.DateTimeField(
        verbose_name="date of approval",
        null=False,
    )

    response = models.OneToOneField(
        ProtocolResponse,
        on_delete=models.CASCADE,
        related_name="response",
    )

def sendemail(sender,**kwargs):
    if kwargs['created']:
        protocol_response_instance = kwargs['instance'].response
        protocol_request_instance = protocol_response_instance.protocolrequest
        #send_email(protocol_request_instance.pi_email, response=True, approved=True)


post_save.connect(sendemail, sender=Protocol)

