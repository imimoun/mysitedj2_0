from django.urls import include, path
from django.views.generic import RedirectView

from api import views

urlpatterns = [
    path('client', views.ClientList.as_view(), name='client-list'),
    path('client/<uuid:uuid>', views.ClientDetail.as_view(), name='client-detail'),
    path('api-auth/', include('rest_framework.urls')),
    path('client',
         RedirectView.as_view(pattern_name='client-list', permanent=True),
         name='index-client-list'),
]
