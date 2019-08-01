from .models import ProtocolResponse, ProtocolRequest, Protocol
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import datetime
from .email import send_email


class ApproveProtocol:

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

    def approve(self, protocol_request=None):
        """Returns True if a protocol is approved and creates a protocol instance.

        :param protocol_request:
        :return:
        """
        protocol_response = protocol_request.request
        approved = False

        if protocol_response.status == "A":  # check if this instance is approved
            messages.success("protocol already approved")
        else:
            # change the status of the response to approved
            try:
                ProtocolResponse.objects.filter(pk=protocol_response.id).update(status='A')
                protocol_response.status = "A"
            except ObjectDoesNotExist:
                ProtocolResponse.objects.create(protocolrequest=protocol_request,
                                                status="A",
                                                response_date=datetime.date.today()
                                                )

            # create a protocol instance once the request has been approved
            Protocol.objects.create(
                name=protocol_request.name,
                number=self.assign_protocol_number(),
                approval_date=timezone.now(),
                response=protocol_response
            )
            # send_email(response=True,approved=True)
            approved = True

        return approved

    def reject(self, protocol_request=None, reason=""):
        """
        reject a protocol requeset and notify an admin
        :param protocol_request:
        :return:
        """
        rejected = False
        protocol_response = protocol_request.request
        if protocol_response.status == "A":  # check if this instance is approved
            messages.success("protocol already approved")
        else:
            try:
                # update the status field of the request object
                ProtocolResponse.objects.filter(pk=protocol_response.id).update(status='R')
                protocol_response.status = "R"
            except ObjectDoesNotExist:
                ProtocolResponse.objects.create(protocolrequest=protocol_request,
                                                status="R",
                                                response_date=datetime.date.today()
                                                )
            rejected = True
            # send_email(response=True, approved=False, reason)
        return rejected