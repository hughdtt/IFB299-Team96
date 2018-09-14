from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^confirm/', views.confirm_res, name='confirm_res')

    ]


