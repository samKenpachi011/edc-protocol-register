from django.db import models

from .protocol_response import ProtocolResponse
from ..validators import validate_protocol_number


class Protocol(models.Model):

    protocol_response = models.OneToOneField(
        ProtocolResponse,
        on_delete=models.CASCADE,
        related_name="response",
    )

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
