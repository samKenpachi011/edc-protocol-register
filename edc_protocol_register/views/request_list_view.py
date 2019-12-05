from django.views.generic import ListView

from ..models import ProtocolRequest
from .home_view import EdcBaseViewMixin



class RequestListView(EdcBaseViewMixin, ListView):

    model = ProtocolRequest
    context_object_name = 'ProtocolRequest'
    template_name = 'edc_protocol_register/request_list.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)