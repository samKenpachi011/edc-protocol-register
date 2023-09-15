from django.views.generic import ListView

from ..models import ProtocolRequest
from .home_view import EdcBaseViewMixin


class RequestListView(EdcBaseViewMixin, ListView):

    model = ProtocolRequest
    context_object_name = 'protocol_request'
    template_name = 'edc_protocol_register/request_list.html'

    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
