from django.db import models

# Create your models here.
class Table1(models.Model):
    order_id = models.IntegerField(db_column='Order_ID', blank=True, null=False, primary_key=True) 
    order_createdate = models.IntegerField(db_column='Order_CreateDate', blank=True, null=True) 
    order_pickupdate = models.IntegerField(db_column='Order_PickupDate', blank=True, null=True) 
    order_pickupstore = models.IntegerField(db_column='Order_PickupStore', blank=True, null=True) 
    pickup_store_name = models.CharField(db_column='Pickup_Store_Name', max_length=21, blank=True, null=True) 
    pickup_store_address = models.CharField(db_column='Pickup_Store_Address', max_length=25, blank=True, null=True) 
    pickup_store_phone = models.CharField(db_column='Pickup_Store_Phone', max_length=19, blank=True, null=True) 
    pickup_store_city = models.CharField(db_column='Pickup_Store_City', max_length=30, blank=True, null=True) 
    pickup_store_state_name = models.CharField(db_column='Pickup_Store_State_Name', max_length=15, blank=True, null=True) 
    order_returndate = models.IntegerField(db_column='Order_ReturnDate', blank=True, null=True) 
    order_returnstore = models.IntegerField(db_column='Order_ReturnStore', blank=True, null=True) 
    return_store_name = models.CharField(db_column='Return_Store_Name', max_length=21, blank=True, null=True) 
    return_store_address = models.CharField(db_column='Return_Store_Address', max_length=25, blank=True, null=True) 
    return_store_phone = models.CharField(db_column='Return_Store_Phone', max_length=19, blank=True, null=True) 
    return_store_city = models.CharField(db_column='Return_Store_City', max_length=30, blank=True, null=True) 
    return_store_state = models.CharField(db_column='Return_Store_State', max_length=15, blank=True, null=True) 
    customer_id = models.IntegerField(db_column='Customer_ID', blank=True, null=True) 
    customer_name = models.CharField(db_column='Customer_Name', max_length=12, blank=True, null=True) 
    customer_phone = models.CharField(db_column='Customer_Phone', max_length=19, blank=True, null=True) 
    customer_addresss = models.CharField(db_column='Customer_Addresss', max_length=30, blank=True, null=True) 
    customer_brithday = models.CharField(db_column='Customer_Brithday', max_length=10, blank=True, null=True) 
    customer_occupation = models.CharField(db_column='Customer_Occupation', max_length=10, blank=True, null=True) 
    customer_gender = models.CharField(db_column='Customer_Gender', max_length=3, blank=True, null=True) 
    car_id = models.IntegerField(db_column='Car_ID', blank=True, null=True) 
    car_makename = models.CharField(db_column='Car_MakeName', max_length=13, blank=True, null=True) 
    car_model = models.CharField(db_column='Car_Model', max_length=15, blank=True, null=True) 
    car_series = models.CharField(db_column='Car_Series', max_length=35, blank=True, null=True) 
    car_seriesyear = models.CharField(db_column='Car_SeriesYear', max_length=4, blank=True, null=True) 
    car_pricenew = models.CharField(db_column='Car_PriceNew', max_length=6, blank=True, null=True) 
    car_enginesize = models.CharField(db_column='Car_EngineSize', max_length=4, blank=True, null=True) 
    car_fuelsystem = models.CharField(db_column='Car_FuelSystem', max_length=18, blank=True, null=True) 
    car_tankcapacity = models.CharField(db_column='Car_TankCapacity', max_length=5, blank=True, null=True) 
    car_power = models.CharField(db_column='Car_Power', max_length=5, blank=True, null=True) 
    car_seatingcapacity = models.CharField(db_column='Car_SeatingCapacity', max_length=2, blank=True, null=True) 
    car_standardtransmission = models.CharField(db_column='Car_StandardTransmission', max_length=5, blank=True, null=True) 
    car_bodytype = models.CharField(db_column='Car_BodyType', max_length=14, blank=True, null=True) 
    car_drive = models.CharField(db_column='Car_Drive', max_length=3, blank=True, null=True)  
    car_wheelbase = models.CharField(db_column='Car_Wheelbase', max_length=6, blank=True, null=True) 
    
    class Meta:
        db_table = 'Rawdata'


