from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'tester/', views.TesterCreate.as_view(success_url=('/searchpage/')), name='tester'),
    url(r'thanks/', views.thanks, name='thanks'),
    ]


