from .models import ProtocolRequest
import csv


def read_and_create():
    with open("") as f:
        reader = csv.reader(f)
        for row in reader:
            ProtocolRequest.objects.create(
                name
            )
