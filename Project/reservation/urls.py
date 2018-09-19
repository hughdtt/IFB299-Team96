from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$',details, name='details'),
    url(r'index/',index, name='index'),
    url(r'reservation_form/', ReserveCreate.as_view(success_url=('reservation_form/')), name='form'),
    ]


