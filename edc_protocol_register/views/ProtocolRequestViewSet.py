from rest_framework import viewsets
from ..models import ProtocolRequest
from  ..serializers import ProtocolRequestSerializer

class ProtocolRequestViewSet(viewsets.ModelViewSet):
    queryset = ProtocolRequest.objects.all()
    serializer_class = ProtocolRequestSerializer