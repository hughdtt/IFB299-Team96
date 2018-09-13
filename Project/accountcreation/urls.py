from django.urls import path
from .views import AccountCreationView

urlpatterns = [
    path('', AccountCreationView.as_view(), name='accountcreation'),
    ]
