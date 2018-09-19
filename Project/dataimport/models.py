from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length = 200,blank=True,null=True)
    customer_phone = models.CharField(max_length=20,blank=True,null=True)
    customer_address = models.CharField(max_length=200,blank=True,null=True)
    customer_birthday = models.DateField(blank=True,null=True)
    customer_occupation = models.CharField(max_length = 30,blank=True,null=True)
    customer_gender = models.CharField(max_length = 5,blank=True,null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Customers.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customers.save()

class Stores(models.Model):
    store_id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length = 200)
    store_address = models.CharField(max_length = 200)
    store_phone = models.CharField(max_length = 20)
    store_city = models.CharField(max_length = 200)
    store_state = models.CharField(max_length = 50)
    def __str__(self):
        return str(self.store_id) + ":" + self.store_name

class Cars(models.Model):
    car_id = models.IntegerField(primary_key=True)
    car_make = models.CharField(max_length = 200)
    car_model = models.CharField(max_length = 200)
    car_series = models.CharField(max_length = 200)
    car_seriesyear = models.IntegerField()
    car_pricenew = models.IntegerField()
    car_enginesize = models.CharField(max_length = 5)
    car_fuelsystem = models.CharField(max_length = 100)
    car_tankcapacity = models.CharField(max_length = 5)
    car_power = models.CharField(max_length = 5)
    car_seatingcapacity = models.IntegerField()
    car_standardtransmission = models.CharField(max_length = 10)
    car_bodytype = models.CharField(max_length = 20)
    car_drive = models.CharField(max_length = 5)
    car_wheelbase = models.CharField(max_length=10)
    def __str__(self):
        return str(self.car_id) + ":" + self.car_make

class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_createdate = models.DateField()
    order_pickupdate = models.DateField()
    order_returndate = models.DateField()
    order_pickupstore = models.ForeignKey(Stores, related_name='PickUpStore', on_delete=models.CASCADE)
    order_returnstore = models.ForeignKey(Stores, related_name='ReturnStore', on_delete=models.CASCADE)
    order_customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    order_car = models.ForeignKey(Cars, on_delete=models.CASCADE)
