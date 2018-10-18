from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
#Model for Reviews
class Reviews(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comment_author", on_delete=models.CASCADE)

    #Generic Foreign Key
    content_type = models.ForeignKey(ContentType, related_name="comment_contenttype",  on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    #Content and DateTime
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author.username) + ":" + str(self.object_id)


#Model for customer
#Has fields for name, phone, address, birthday, occupation, and gender
#Has a one to one link with the built in django user object
class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Links customer to user object
    customer_name = models.CharField(max_length = 200,blank=True,null=True)
    customer_phone = models.CharField(max_length=20,blank=True,null=True)
    customer_address = models.CharField(max_length=200,blank=True,null=True)
    customer_birthday = models.DateField(blank=True,null=True)
    customer_occupation = models.CharField(max_length = 30,blank=True,null=True)
    customer_gender = models.CharField(max_length = 5,blank=True,null=True)
    def __str__(self):  #Returns the customer's name
        return str(self.customer_name)

#Whenever a user object is created, it creates an accompanying empty customer object, linked to it
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Customers.objects.create(user=instance)

#Whenever a user object is saved, the accompanying customer object is also saved.
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customers.save()

#Model for store
#Has fields for ID,name,address,phone,city, and state
class Stores(models.Model):
    store_id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length = 200)
    store_address = models.CharField(max_length = 200)
    store_phone = models.CharField(max_length = 20)
    store_city = models.CharField(max_length = 200)
    store_state = models.CharField(max_length = 50)
    def __str__(self):  #Returns the store's ID and name
        return str(self.store_id) + ":" + self.store_name

#Model for cars
#Has fields for ID,make,model, series, and more info about the car.
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
    comment_body = models.TextField(blank=True)
    comments = GenericRelation(Reviews)
    def __str__(self):  #Returns the car's make
        return str(self.car_id) + ":" + self.car_make

    


#Model for orders
#Has fields linking it to the pickup store, return store, customer, and car, as well as the dates for creation, pickup, and return.
class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_createdate = models.DateField(auto_now_add=True)
    order_pickupdate = models.DateField()
    order_returndate = models.DateField()
    order_pickupstore = models.ForeignKey(Stores, related_name='PickUpStore', on_delete=models.CASCADE)
    order_returnstore = models.ForeignKey(Stores, related_name='ReturnStore', on_delete=models.CASCADE)
    order_customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    order_car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    def __str__(self):  #Returns the order's id
        return str(self.order_id) + ":" + str(self.order_createdate) + ":" + str(self.order_customer)


