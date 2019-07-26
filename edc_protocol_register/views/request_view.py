from django.views.generic import CreateView
from edc_base.view_mixins import EdcBaseViewMixin
from ..models import ProtocolRequest
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class RequestView(EdcBaseViewMixin, CreateView):

    template_name = 'edc_protocol_register/apply.html'
    model = ProtocolRequest
    fields = ['name', 'description', 'email', 'pi_email', 'duration']

    def form_valid(self, form):
        request = super(RequestView, self).save(commit=False)
        self.request.save()
        return HttpResponseRedirect(self.get_success_url())