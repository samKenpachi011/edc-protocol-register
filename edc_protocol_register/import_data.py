from .models import ProtocolRequest
import csv
from django.utils.timezone import datetime
from .approvalManager import ApproveProtocol

ap = ApproveProtocol()

def read_and_create_request():
    with open("BHP_Studies.csv") as f:
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

