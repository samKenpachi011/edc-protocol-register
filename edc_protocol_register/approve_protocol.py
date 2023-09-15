from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from .models import Protocol


class ApproveProtocol:

    def email_notification(self, message=None, subject=None, to_emails=[]):
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # FROM
            to_emails,  # TO
            fail_silently=False)

    def assign_protocol_number(self):
        """Returns the next available protocol number.

        :return: protocol number
        """
        last_protocol_number = 0
        new_number = 0
        protocol = Protocol.objects.all().order_by('number').last()
        if protocol:
            last_protocol_number = protocol.number
            new_number = last_protocol_number + 1
        else:
            new_number = 1
        return new_number

    def approve(self, protocol_response=None):
        """Returns True if a protocol is approved and creates a protocol instance.

        :param protocol_request:
        :return:
        """
        approved = False

        if protocol_response.status == "A":
            # create a protocol instance once the request has been approved
            try:
                Protocol.objects.get(protocol_response=protocol_response)
            except Protocol.DoesNotExist:
                protocol_number = self.assign_protocol_number()
                Protocol.objects.create(
                    short_name=protocol_response.protocol_request.short_name,
                    long_name=protocol_response.protocol_request.long_name,
                    number=protocol_number,
                    approval_date=timezone.now(),
                    protocol_response=protocol_response
                )
                message = f"Your request for a protocol number for the project {protocol_response.protocol_request.long_name}has been apporved and you protocol number is: {protocol_number}"
                subject = f"Protocol request for {protocol_response.protocol_request.short_name}"
                emails = [
                    protocol_response.protocol_request.pi_email,
                    protocol_response.protocol_request.email]
                self.email_notification(
                    message=message,
                    subject=subject,
                    to_emails=emails)
                approved = True

        return approved

    def reject(self, protocol_response=None):
        """
        reject a protocol requeset and notify an admin
        :param protocol_request:
        :return:
        """
        rejected = False
        if protocol_response.status == "R":
            rejected = True
            message = f"Your request for a protocol number for the project {protocol_response.protocol_request.long_name}has been rejected and you protocol number is: {protocol_number}. Please contact the Data management center"
            subject = f"Protocol request for {protocol_response.protocol_request.short_name}"
            try:
                Protocol.objects.get(
                    protocol_response=protocol_response).delete()
            except Protocol.DoesNotExist:
                pass
            emails = [
                protocol_response.protocol_request.pi_email,
                protocol_response.protocol_request.email]
            self.email_notification(
                message=message,
                subject=subject,
                to_emails=emails)
        return rejected
