from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^obtain-token/$', views.ObtainTokenView.as_view(), name='obtain_token'),
    url(r'^invalidate-token/$', views.InvalidateTokenView.as_view(), name='invalidate_token'),
]
