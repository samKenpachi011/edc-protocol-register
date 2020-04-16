from django.apps import apps as django_apps
from django.conf import settings
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin

from django_revision.views import RevisionMixin

from edc_navbar import NavbarViewMixin


class EdcBaseViewMixin(RevisionMixin, ContextMixin):
    """Mixes in common template variables for the footer, etc.
    """

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        app_config = django_apps.get_app_config('edc_base')
        edc_device_app_config = django_apps.get_app_config('edc_device')
        context = super().get_context_data(**kwargs)
        try:
            live_system = settings.LIVE_SYSTEM
        except AttributeError:
            live_system = None
        context.update({
            'DEBUG': settings.DEBUG,
            'copyright': app_config.copyright,
            'device_id': edc_device_app_config.device_id,
            'device_role': edc_device_app_config.device_role,
            'disclaimer': app_config.disclaimer,
            'institution': app_config.institution,
            'license': app_config.license,
            'project_name': app_config.project_name,
            'live_system': live_system})
        try:
            if settings.WARNING_MESSAGE:
                messages.add_message(
                    self.request, messages.WARNING, settings.WARNING_MESSAGE,
                    extra_tags='warning')
        except AttributeError:
            pass
        return context


class HomeView(EdcBaseViewMixin, NavbarViewMixin, TemplateView):

    template_name = 'edc_protocol_register/home.html'
    navbar_name = 'protocols'
    navbar_selected_item = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update()
        return context

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)