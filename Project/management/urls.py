#pages/urls.py
from django.urls import path

from .views import ManagementPageView

urlpatterns = [
    path('management/', ManagementPageView.as_view(), name='management'),
    ]
