from django.test import TestCase
# from edc_protocol_register.models import Protocol
from edc_protocol_register.models import ProtocolRequest
# from edc_protocol_register.models import ProtocolResponse
from edc_protocol_register.forms import ProtocolRequestForm
from edc_protocol_register.approve_protocol import ApproveProtocol
from faker import Faker


fake = Faker()
ap = ApproveProtocol()


def create_request():
    return ProtocolRequest.objects.create(
        short_name="abc",
        long_name='abc',
        description=fake.text(),
        email=fake.email(), pi_email=fake.email(),
        request_date="2019-02-02",
        )


class ProtocolRequestTest(TestCase):

    def test_ProtocolRequestForm_valid(self):
        form = ProtocolRequestForm(
            data={'short_name': "qwert",
                  'long_name': 'sadfadfas',
                  'description': "sadfasdfasdf",
                  'email': "salah@gmail.com",
                  'pi_email': "salah@gmail.com",
                  'request_date': '2019-02-02'})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_ProtocolRequestForm_invalid(self):
        form = ProtocolRequestForm(
            data={'short_name': "",
                  'long_name': '',
                  'description': "sadfasdfasdf",
                  'email': "salah@gmail.com",
                  'pi_email': "salah@gmail.com",
                  'request_date': 'A'})
        self.assertFalse(form.is_valid())

    # testing email validator
    def test_ProtocolRequestForm_with_invalid_email(self):
        form = ProtocolRequestForm(
            data={'short_name': "qwert",
                  'description': "sadfasdfasdf",
                  'pi_email': "salah"})
        self.assertFalse(form.is_valid())


# class ProtocolApprovalTest(TestCase):

#     # creating a protocol request object

#     # testing if instant of type Protocolresponse is created when a request is made
#     def test_request_creation(self):
#         options = {
#             'short_name': 'BCPP',
#             'long_name': 'Botswana Combination Prevension Project',
#             'description': 'this is a description',
#             'email': 'bhcp@gmail.com',
#             'pi_email': 'bhcp@gmail.com',
#             'request_date': '2019-02-02'
#         }

#         protocol_request.objects.create(**options)
#         self.assertEqual(protocol_response.objects.all().count(), 1)

#     def test_response_instance_creation(self):
#         options = {
#             'short_name': 'BCPP',
#             'long_name': 'Botswana Combination Prevension Project',
#             'description': 'this is a description',
#             'email': 'bhcp@gmail.com',
#             'pi_email': 'bhcp@gmail.com',
#             'request_date': '2019-02-02'
#         }
#         protocol_request = protocol_request.objects.create(**options)
#         self.assertTrue(isinstance(protocol_request.request, protocol_response))


#     def test_protocol_approval(self):
#         options = {
#             'short_name': 'BCPP',
#             'long_name': 'Botswana Combination Prevension Project',
#             'description': 'this is a description',
#             'email': 'bhcp@gmail.com',
#             'pi_email': 'bhcp@gmail.com',
#             'request_date': '2019-02-02'
#         }
#         protocol_request = protocol_request.objects.create(**options)
#         ap.approve(protocol_request)
#         protocol_response = protocol_request.request
#         self.assertEqual(protocol_response.status, "A")
#         # test if a protocol instance has been created
#         self.assertTrue(isinstance(protocol_response.response, protocol))

#     def test_protocol_rejection(self):
#         options = {
#             'short_name': 'BCPP',
#             'long_name': 'Botswana Combination Prevension Project',
#             'description': 'this is a description',
#             'email': 'bhcp@gmail.com',
#             'pi_email': 'bhcp@gmail.com',
#             'request_date': '2019-02-02'
#         }
#         protocol_request = protocol_request.objects.create(**options)
#         ap.reject(protocol_request)
#         protocol_response = protocol_request.request
#         self.assertEqual(protocol_response.status, "R")

#     def test_response_creation(self):
#         options = {
#             'short_name': 'BCPP',
#             'long_name': 'Botswana Combination Prevension Project',
#             'description': 'this is a description',
#             'email': 'bhcp@gmail.com',
#             'pi_email': 'bhcp@gmail.com',
#             'request_date': '2019-02-02'
#         }
#         protocol_request = protocol_request.objects.create(**options)
#         response = protocol_request.request
#         self.assertTrue(response.status, "P")

#     # testing if all the protocol instances are approved
#     def test_request_approval(self):
#         [self.assertEqual(x.response.status, "A") for x in protocol.objects.all()]

#     def test_duplicate_protocol_number(self):
#         no_dup = set()
#         a = protocol.objects.all()
#         for i in a:
#             no_dup.add(i.number)
#         self.assertEqual(len(no_dup), len(a))
