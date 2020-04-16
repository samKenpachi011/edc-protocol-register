from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView

from edc_protocol_register.forms import protocol_request_form
from ..models import ProtocolRequest
from .home_view import EdcBaseViewMixin


class RequestView(EdcBaseViewMixin, CreateView):

    template_name = 'edc_protocol_register/apply.html'
    model = ProtocolRequest
    form_class = protocol_request_form
    success_url = reverse_lazy('home_url')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.request_date = timezone.now()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)