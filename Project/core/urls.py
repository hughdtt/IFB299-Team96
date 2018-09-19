from django.urls import path

from . import views
#Index (home) page
urlpatterns = [
    path('', views.index, name='index'),
]