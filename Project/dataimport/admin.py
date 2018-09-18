from django.contrib import admin

# Register your models here.
from .models import Customers, Stores, Cars, Orders

admin.site.register(Customers)
admin.site.register(Stores)
admin.site.register(Cars)
admin.site.register(Orders)