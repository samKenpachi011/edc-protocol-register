from django import forms
from ..models import ProtocolRequest


class DateInput(forms.DateInput):
    input_type = 'date'


class ProtocolRequestForm(forms.ModelForm):

    class Meta:
        model = ProtocolRequest
        fields = ['short_name', 'long_name', 'description', 'email', 'pi_email', 'request_date', 'duration']
