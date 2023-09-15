import csv
from django.utils.timezone import datetime

from ..models import ProtocolRequest
from ..approve_protocol import ApproveProtocol

ap = ApproveProtocol()


def read_and_create_request(request):
    file_path = ("/Users/salahdinzeberga/PycharmProjects/"
                 "edc-protocol-register/edc_protocol_register/"
                 "views/BHP_Studies.csv")
    with open(file_path, 'r') as f:
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
