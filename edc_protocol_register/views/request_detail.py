from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

from edc_base.view_mixins.edc_base_view_mixin import EdcBaseViewMixin

from ..models import ProtocolRequest


class ProtocolRequestDetailView(EdcBaseViewMixin,DetailView):

    template_name = 'edc_protocol_register/detail_view.html'
    queryset = ProtocolRequest.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(ProtocolRequest, id=id_)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

