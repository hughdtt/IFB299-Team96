from django.urls import path
from django.conf.urls import url

from . import views
#Index (home) page
urlpatterns = [
    path('', views.index, name='home'),
    url(r'thanks/',views.thanks, name='thanks_page'),
]