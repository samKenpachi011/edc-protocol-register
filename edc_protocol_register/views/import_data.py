from edc_protocol_register.models import ProtocolRequest
import csv
from django.utils.timezone import datetime
from edc_protocol_register.approvalManager import ApproveProtocol

ap = ApproveProtocol()

def read_and_create_request(request):
    with open("/Users/salahdinzeberga/PycharmProjects/edc-protocol-register/edc_protocol_register/views/BHP_Studies.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            P_request = ProtocolRequest.objects.create(
                name=row[0],
                description=row[1],
                email='default@default.com',
                pi_email='default@default.com',
                request_date=datetime.now(),
            )

            ap.approve(P_request)

