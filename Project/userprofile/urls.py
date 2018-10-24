from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.profile, name='profile'),
	url(r'profile/',views.profile, name='profile_page'),

]