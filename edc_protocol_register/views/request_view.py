from django.views.generic import CreateView
from edc_base.view_mixins import EdcBaseViewMixin
from ..models import ProtocolRequest
from ..forms import ProtocolRequestForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone


class RequestView(EdcBaseViewMixin, CreateView):

    template_name = 'edc_protocol_register/apply.html'
    model = ProtocolRequest
    form_class = ProtocolRequestForm
    success_url = reverse_lazy('home_url')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.request_date = timezone.now()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())