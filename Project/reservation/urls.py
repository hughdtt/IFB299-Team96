from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.details, name='index'),
    url(r'reservation_form/', views.ReserveCreate.as_view(success_url=('reservation_form/')), name='form'),
    ]


