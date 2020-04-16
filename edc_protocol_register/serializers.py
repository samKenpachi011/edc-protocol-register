from rest_framework import serializers
from edc_protocol_register.models import protocol_request


class ProtocolRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = protocol_request
        fields = '__all__'

