from django.apps import apps as django_apps
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import datetime


def validate_pi_email(value):
    try:
        EmailValidator(value)
    except ValidationError:
        raise ValidationError('Enter a valid email address.')

    return value


def validate_protocol_number(value):
    protocol_model_cls = django_apps.get_model('edc_protocol_register.protocol')
    lst = [x.number for x in protocol_model_cls.objects.all()]
    if value in lst:
        raise ValidationError('number already taken.')
    elif value < 0:
        raise ValidationError('invalid number')
    else:
        return value


def validate_protocol_request_date(value):
    if value < datetime.date.today():
        raise ValidationError('invalid date.')
    else:
        return value
