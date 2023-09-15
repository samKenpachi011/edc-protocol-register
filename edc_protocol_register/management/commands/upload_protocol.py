import csv

from django.core.management.base import BaseCommand
from django.utils import timezone

from ...models import ProtocolRequest, ProtocolResponse, Protocol


class ProtocolError(Exception):
    pass


class Command(BaseCommand):
    help = 'Creates protocols'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def readfiles(self, fpath=None):
        lines = []
        with open(fpath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                lines.append(row)
        return lines

    def handle(self, *args, **options):
        fpath = options['file_path']
        print(fpath, '&&&&&&&&&&')
        protocols_data = self.readfiles(fpath=fpath)
        del protocols_data[0]
        invalid_protocol_numbers = -1
        protocols_created = 0
        for pl in protocols_data:
            number, short_name, long_name, description,  _ = pl
            if number:
                try:
                    number = int(number)
                except ValueError:
                    if isinstance(number, str):
                        short_name += ' ' + number
                        number = invalid_protocol_numbers
                        invalid_protocol_numbers += -1
            else:
                number = invalid_protocol_numbers
                invalid_protocol_numbers += -1
            try:
                ProtocolRequest.objects.get(
                    short_name=short_name, long_name=long_name)
            except ProtocolRequest.DoesNotExist:
                protocol_request = ProtocolRequest(
                    short_name=short_name,
                    long_name=long_name,
                    description=description)
                protocol_request.save_base(raw=True)
                try:
                    ProtocolResponse.objects.get(
                        protocol_request=protocol_request)
                except ProtocolResponse.DoesNotExist:
                    protocol_response = ProtocolResponse(
                        protocol_request=protocol_request,
                        status='A',
                        response_date=timezone.now())
                    protocol_response.save_base(raw=True)
                    try:
                        Protocol.objects.get(number=number)
                    except Protocol.DoesNotExist:
                        Protocol.objects.create(
                            short_name=short_name,
                            long_name=protocol_response.protocol_request.long_name,
                            number=number,
                            approval_date=timezone.now(),
                            protocol_response=protocol_response)
                        self.stdout.write(self.style.SUCCESS(
                            f'Protocol {short_name} has been successfully created'))
                        protocols_created += 1
        self.stdout.write(self.style.SUCCESS(
            f'Successfully created {protocols_created} protocols'))
