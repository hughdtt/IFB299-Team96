from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_phone = models.CharField(max_length=20)
    customer_address = models.CharField(max_length=200)
    customer_birthday = models.DateField()
    customer_occupation = models.CharField(max_length = 30)
    customer_gender = models.CharField(max_length = 1)
    def __str__(self):
        return str(self.customer_id) + ":" + self.customer_name


