from django.urls import path
from . import views

#Goes to the CSV import page
urlpatterns = [
    path('', views.index, name='dataimportindex'),
]
