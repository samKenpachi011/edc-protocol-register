from django.db import models
from .protocol_request import ProtocolRequest


STATUS = (
    ('P', 'Pending'),
    ('A', 'Approved'),
    ('R', 'Rejected')
)


class ProtocolResponse(models.Model):

    protocol_request = models.OneToOneField(
        ProtocolRequest,
        on_delete=models.CASCADE,
        related_name="request",
        null=True
    )

    status = models.CharField(
        verbose_name="protocol status",
        max_length=50,
        choices=STATUS,
        default="P"
    )

    response_date=models.DateField(
        verbose_name="date of response",
    )

    def __str__(self):
        return self.status
