from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'reservation_form/', views.ReserveCreate.as_view(success_url=('/searchpage/')), name='form'),
    ]


