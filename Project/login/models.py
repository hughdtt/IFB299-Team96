from django.db import models

# Create your models here.

class Customers(models.Model):
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=20)
    customer_address = models.CharField(max_length=200)
    customer_birthday = models.DateField()
    customer_occupation = models.CharField(max_length = 30)
    customer_gender = models.CharField(max_length = 1)
