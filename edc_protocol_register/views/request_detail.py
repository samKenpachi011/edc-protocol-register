from ..models import ProtocolRequest
from django.shortcuts import get_object_or_404
from edc_base.view_mixins import EdcBaseViewMixin
from django.views.generic.detail import DetailView


class ProtocolRequestDetailView(EdcBaseViewMixin,DetailView):

    template_name = 'edc_protocol_register/detail_view.html'
    queryset = ProtocolRequest.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(ProtocolRequest, id=id_)

