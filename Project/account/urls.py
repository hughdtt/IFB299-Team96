from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

#Adds the login, logout, and register view
#Uses the built in Django login/logout templates
urlpatterns = [
    path('loggedin/', views.loggedin, name='loggedin'),
    path('register/', views.create, name='create'),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
]
