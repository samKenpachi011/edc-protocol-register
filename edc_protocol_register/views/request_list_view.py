from django.views.generic import ListView
from edc_base.view_mixins import EdcBaseViewMixin
from ..models import ProtocolRequest


class RequestListView(EdcBaseViewMixin, ListView):

    model = ProtocolRequest
    context_object_name = 'ProtocolRequest'
    template_name = 'edc_protocol_register/request_list.html'
    paginate_by = 4
