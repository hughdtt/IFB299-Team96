from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url

#Adds the login, logout, and register view
#Uses the built in Django login/logout templates
urlpatterns = [
    path('loggedin/', views.loggedin, name='loggedin'),
    path('register/', views.create, name='create'),
    url(r'register_2/',views.create_customer, name='create_customer'),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
]
