"""edc_protocol_register URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls.conf import path, include

from .views import HomeView,\
    AdministrationView,\
    RequestView, RequestListView, ProtocolRequestDetailView, approve_request, reject_request, read_and_create_request

from .admin_site import edc_protocol_register_admin

app_name = 'edc_protocol_register'

urlpatterns = [
    path('accounts/', include('edc_base.auth.urls')),
    path('admin/', include('edc_base.auth.urls')),
    path('admin/', admin.site.urls),
    path('admin/', edc_protocol_register_admin.urls),

    path('administration/', AdministrationView.as_view(),
         name='administration_url'),
    path('edc_base/', include('edc_base.urls')),
    path('edc_device/', include('edc_device.urls')),

    path('switch_sites/', LogoutView.as_view(next_page=settings.INDEX_PAGE),
         name='switch_sites_url'),
    path('home/', HomeView.as_view(), name='search_url'),
    path('home/', HomeView.as_view(), name='home_url'),
    path('', HomeView.as_view(), name='home_url'),

    path('apply/', RequestView.as_view(), name='request_url'),
    path('list/', RequestListView.as_view(), name='request_list'),

    path('detail/<int:id>', ProtocolRequestDetailView.as_view(),
         name='request_detail'),
    path('approve/<int:id>', approve_request, name='approve'),
    path('reject/<int:id>', reject_request, name='reject'),
    path('load/', read_and_create_request, name='create')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
