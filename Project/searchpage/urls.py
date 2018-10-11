from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('results/', views.results, name='results'),


]
    
