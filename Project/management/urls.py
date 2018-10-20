#pages/urls.py
from django.urls import path

from .views import ManagementPageView
from . import views

urlpatterns = [
    path('management/', ManagementPageView.as_view(), name='management'),
    path('analytics/', views.analytics, name='analytics'),
    path('store/', views.store, name = 'store')
    ]
