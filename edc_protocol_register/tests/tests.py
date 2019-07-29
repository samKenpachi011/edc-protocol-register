from django.test import TestCase
from ..models import Protocol
from ..models import ProtocolRequest
from ..models import ProtocolResponse
from ..forms import ProtocolRequestForm
from django.urls import reverse
from ..approvalManager import ApproveProtocol
from faker import Faker


fake = Faker()
ap = ApproveProtocol()


def create_request():
    return ProtocolRequest.objects.create(name="abc",
                                          description=fake.text(),
                                          email=fake.email(), pi_email=fake.email(),
                                          request_date="2019-02-02",
                                          )


class ProtocolRequestTest(TestCase):

    def test_ProtocolRequestForm_valid(self):
        form = ProtocolRequestForm(data={'name': "qwert", 'description': "sadfasdfasdf", 'email': "salah@gmail.com",
                                         'pi_email': "salah@gmail.com", 'request_date': '2019-02-02'})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_ProtocolRequestForm_invalid(self):
        form = ProtocolRequestForm(data={'name': "", 'description': "sadfasdfasdf", 'email': "salah@gmail.com",
                                         'pi_email': "salah@gmail.com", 'request_date': 'A'})
        self.assertFalse(form.is_valid())

    # testing email validator
    def test_ProtocolRequestForm_with_invalid_email(self):
        form = ProtocolRequestForm(data={'name': "qwert", 'description': "sadfasdfasdf", 'pi_email': "salah"})
        self.assertFalse(form.is_valid())


class ProtocolApprovalTest(TestCase):

    # creating a protocol request object

    # testing if instant of type Protocolresponse is created when a request is made
    def test_request_creation(self):
        options = {
            'name': 'BCPP',
            'description': 'this is a description',
            'email': 'bhcp@gmail.com',
            'pi_email': 'bhcp@gmail.com',
            'request_date': '2019-02-02'
        }
        protocol_request = ProtocolRequest.objects.create(**options)
        self.assertEqual(ProtocolResponse.objects.all().count(), 1)

    def test_response_instance_creation(self):
        options = {
            'name': 'BCPP',
            'description': 'this is a description',
            'email': 'bhcp@gmail.com',
            'pi_email': 'bhcp@gmail.com',
            'request_date': '2019-02-02'
        }
        protocol_request = ProtocolRequest.objects.create(**options)
        self.assertTrue(isinstance(protocol_request.request, ProtocolResponse))


    def test_protocol_approval(self):
        options = {
            'name': 'BCPP',
            'description': 'this is a description',
            'email': 'bhcp@gmail.com',
            'pi_email': 'bhcp@gmail.com',
            'request_date': '2019-02-02'
        }
        protocol_request = ProtocolRequest.objects.create(**options)
        ap.approve(protocol_request)
        protocol_response = protocol_request.request
        self.assertEqual(protocol_response.status, "A")
        # test if a protocol instance has been created
        self.assertTrue(isinstance(protocol_response.response, Protocol))

    def test_protocol_rejection(self):
        options = {
            'name': 'BCPP',
            'description': 'this is a description',
            'email': 'bhcp@gmail.com',
            'pi_email': 'bhcp@gmail.com',
            'request_date': '2019-02-02'
        }
        protocol_request = ProtocolRequest.objects.create(**options)
        ap.reject(protocol_request)
        protocol_response = protocol_request.request
        self.assertEqual(protocol_response.status, "R")

    def test_response_creation(self):
        options = {
            'name': 'BCPP',
            'description': 'this is a description',
            'email': 'bhcp@gmail.com',
            'pi_email': 'bhcp@gmail.com',
            'request_date': '2019-02-02'
        }
        protocol_request = ProtocolRequest.objects.create(**options)
        response = protocol_request.request
        self.assertTrue(response.status, "P")

    # testing if all the protocol instances are approved
    def test_request_approval(self):
        [self.assertEqual(x.response.status, "A") for x in Protocol.objects.all()]

    def test_duplicate_protocol_number(self):
        no_dup = set()
        a = Protocol.objects.all()
        for i in a:
            no_dup.add(i.number)
        self.assertEqual(len(no_dup), len(a))



