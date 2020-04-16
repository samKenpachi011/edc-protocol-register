from django.db import models
from django.utils import timezone


class ProtocolRequest(models.Model):

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

    description = models.TextField(
        verbose_name="protocol description",
        max_length=500,
        null=False,
        blank=True
    )

    email = models.EmailField(
        verbose_name="email",
        max_length=200,
        null=False,
        blank=False,
    )

    pi_email = models.EmailField(
        verbose_name="PI email",
        max_length=200,
        null=False,
        blank=False,
    )

    request_date = models.DateTimeField(
        verbose_name="requested date",
        default=timezone.now
    )

    duration = models.DurationField(
        verbose_name="duration of study",
        null=True,
        help_text="study duration",
        blank=True,
    )

    def __str__(self):
        return self.short_name

    def snippet(self):
        return self.description[:20] + " ..."

    class Meta:
        ordering = ['-request_date']
        permissions = [
            ('can_approve_request', "user can approve request"),
            ('can_reject_request', "user can reject request")
        ]

