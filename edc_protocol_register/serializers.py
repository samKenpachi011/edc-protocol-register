from rest_framework import serializers
from .models import ProtocolRequest


class ProtocolRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProtocolRequest
        fields = '__all__'

