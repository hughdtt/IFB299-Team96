from django.urls import path
from .views import AccountCreationView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('loggedin/', views.loggedin, name='loggedin'),
    path('register/', AccountCreationView.as_view(), name='accountcreation'),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
]
