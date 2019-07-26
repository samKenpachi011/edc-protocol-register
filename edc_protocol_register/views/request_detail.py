from ..models import ProtocolRequest
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

class ProtocolRequestDetailView(DetailView):

    template_name = 'edc_protocol_register/detail_view.html'
    queryset = ProtocolRequest.objects.all()
    context_object_name = 'request'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(ProtocolRequest, id=id_)