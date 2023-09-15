from rest_framework import viewsets
from ..serializers import ProtocolRequestSerializer
from ..models import ProtocolRequest


class ProtocolRequestViewSet(viewsets.ModelViewSet):
    queryset = ProtocolRequest.objects.all()
    serializer_class = ProtocolRequestSerializer
