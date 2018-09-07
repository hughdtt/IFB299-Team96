# Generated by Django 2.1 on 2018-09-07 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('order_id', models.IntegerField(blank=True, db_column='Order_ID', primary_key=True, serialize=False)),
                ('order_createdate', models.IntegerField(blank=True, db_column='Order_CreateDate', null=True)),
                ('order_pickupdate', models.IntegerField(blank=True, db_column='Order_PickupDate', null=True)),
                ('order_pickupstore', models.IntegerField(blank=True, db_column='Order_PickupStore', null=True)),
                ('pickup_store_name', models.CharField(blank=True, db_column='Pickup_Store_Name', max_length=21, null=True)),
                ('pickup_store_address', models.CharField(blank=True, db_column='Pickup_Store_Address', max_length=25, null=True)),
                ('pickup_store_phone', models.CharField(blank=True, db_column='Pickup_Store_Phone', max_length=19, null=True)),
                ('pickup_store_city', models.CharField(blank=True, db_column='Pickup_Store_City', max_length=30, null=True)),
                ('pickup_store_state_name', models.CharField(blank=True, db_column='Pickup_Store_State_Name', max_length=15, null=True)),
                ('order_returndate', models.IntegerField(blank=True, db_column='Order_ReturnDate', null=True)),
                ('order_returnstore', models.IntegerField(blank=True, db_column='Order_ReturnStore', null=True)),
                ('return_store_name', models.CharField(blank=True, db_column='Return_Store_Name', max_length=21, null=True)),
                ('return_store_address', models.CharField(blank=True, db_column='Return_Store_Address', max_length=25, null=True)),
                ('return_store_phone', models.CharField(blank=True, db_column='Return_Store_Phone', max_length=19, null=True)),
                ('return_store_city', models.CharField(blank=True, db_column='Return_Store_City', max_length=30, null=True)),
                ('return_store_state', models.CharField(blank=True, db_column='Return_Store_State', max_length=15, null=True)),
                ('customer_id', models.IntegerField(blank=True, db_column='Customer_ID', null=True)),
                ('customer_name', models.CharField(blank=True, db_column='Customer_Name', max_length=12, null=True)),
                ('customer_phone', models.CharField(blank=True, db_column='Customer_Phone', max_length=19, null=True)),
                ('customer_addresss', models.CharField(blank=True, db_column='Customer_Addresss', max_length=30, null=True)),
                ('customer_brithday', models.CharField(blank=True, db_column='Customer_Brithday', max_length=10, null=True)),
                ('customer_occupation', models.CharField(blank=True, db_column='Customer_Occupation', max_length=10, null=True)),
                ('customer_gender', models.CharField(blank=True, db_column='Customer_Gender', max_length=3, null=True)),
                ('car_id', models.IntegerField(blank=True, db_column='Car_ID', null=True)),
                ('car_makename', models.CharField(blank=True, db_column='Car_MakeName', max_length=13, null=True)),
                ('car_model', models.CharField(blank=True, db_column='Car_Model', max_length=15, null=True)),
                ('car_series', models.CharField(blank=True, db_column='Car_Series', max_length=35, null=True)),
                ('car_seriesyear', models.CharField(blank=True, db_column='Car_SeriesYear', max_length=4, null=True)),
                ('car_pricenew', models.CharField(blank=True, db_column='Car_PriceNew', max_length=6, null=True)),
                ('car_enginesize', models.CharField(blank=True, db_column='Car_EngineSize', max_length=4, null=True)),
                ('car_fuelsystem', models.CharField(blank=True, db_column='Car_FuelSystem', max_length=18, null=True)),
                ('car_tankcapacity', models.CharField(blank=True, db_column='Car_TankCapacity', max_length=5, null=True)),
                ('car_power', models.CharField(blank=True, db_column='Car_Power', max_length=5, null=True)),
                ('car_seatingcapacity', models.CharField(blank=True, db_column='Car_SeatingCapacity', max_length=2, null=True)),
                ('car_standardtransmission', models.CharField(blank=True, db_column='Car_StandardTransmission', max_length=5, null=True)),
                ('car_bodytype', models.CharField(blank=True, db_column='Car_BodyType', max_length=14, null=True)),
                ('car_drive', models.CharField(blank=True, db_column='Car_Drive', max_length=3, null=True)),
                ('car_wheelbase', models.CharField(blank=True, db_column='Car_Wheelbase', max_length=6, null=True)),
            ],
            options={
                'db_table': 'Rawdata',
            },
        ),
    ]
