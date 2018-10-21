#Reference for the position of objects within the data.csv
'''
0 = Order_ID / Store_ID
1 = Order_CreateDate / Store_Name
2 = Order_PickupDate / Store_Address
3 = Order_PickupStore / Store_Phone
4 = Pickup_Store_Name / Store_City
5 = Pickup_Store_Address / Store_State
6 = Pickup_Store_Phone / Order_ID
7 = Pickup_Store_City / Order_CreateDate
8 = Pickup_Store_State_Name / Pickup_Or_Return
9 = Order_ReturnDate / Pickup_Or_Return_Date
10 = Order_ReturnStore / Customer_ID
11 = Return_Store_Name / Customer_Name
12 = Return_Store_Address / Customer_Phone
13 = Return_Store_Phone / Customer_Address
14 = Return_Store_City / Customer_Birthday
15 = Return_Store_State / Customer_Occupation
16 = Customer_ID / Customer_Gender
17 = Customer_Name / Car_ID
18 = Customer_Phone / Car_MakeName
19 = Customer_Addresss / Car_Model
20 = Customer_Brithday / Car_Series
21 = Customer_Occupation / Car_SeriesYear
22 = Customer_Gender / Car_PriceNew
23 = Car_ID / Car_EngineSize
24 = Car_MakeName / Car_FuelSystem
25 = Car_Model / Car_TankCapacity
26 = Car_Series / Car_Power
27 = Car_SeriesYear / Car_SeatingCapacity
28 = Car_PriceNew / Car_StandardTransmission
29 = Car_EngineSize / Car_Body
30 = Car_FuelSystem / Car_Drive
31 = Car_TankCapacity / Car_Wheelbase
32 = Car_Power
33 = Car_SeatingCapacity
34 = Car_StandardTransmission
35 = Car_BodyType
36 = Car_Drive
37 = Car_Wheelbase
'''

import datetime
import csv
from dataimport.models import *
from django.contrib.auth.models import User
def importthedata(centralOrStore):      
    #1 = central
    #2 = store
    if(centralOrStore == 2):
        filename = 'dataStore.csv'
        sto = True
        sto_id = 0
        sto_name = 1
        sto_address = 2
        sto_phone = 3
        sto_city = 4
        sto_state = 5
        
        cust_id = 10
        cust_name = 11
        cust_phone = 12
        cust_address = 13
        cust_birthday = 14
        cust_occupation = 15
        cust_gender = 16
        cr_id = 17
        cr_make = 18
        cr_model = 19
        cr_series = 20
        cr_seriesyear = 21
        cr_pricenew = 22
        cr_enginesize = 23
        cr_fuelsystem = 24
        cr_tank = 25
        cr_power = 26
        cr_seating = 27
        cr_standardtransmission = 28
        cr_body = 29
        cr_drive = 30
        cr_wheelbase = 31

    else:
        filename = 'data.csv'
        sto = False
        cust_id = 16
        cust_name = 17
        cust_phone = 18
        cust_address = 19
        cust_birthday = 20
        cust_occupation = 21
        cust_gender = 22
        cr_id = 23
        cr_make = 24
        cr_model = 25
        cr_series = 26
        cr_seriesyear = 27
        cr_pricenew = 28
        cr_enginesize = 29
        cr_fuelsystem = 30
        cr_tank = 31
        cr_power = 32
        cr_seating = 33
        cr_standardtransmission = 34
        cr_body = 35
        cr_drive = 36
        cr_wheelbase = 37
    with open(filename, newline='') as csvfile:   #Opens the CSV file , with delimiter ','
        datareader = csv.reader(csvfile, delimiter=',')       
        a = 0
        for row in datareader:   #Iterates through every row in the CSV file 
            if(a > 0):  #Ignores the first row, as it contains the heading for the data
                # Adding Customers  
                #print("Now adding:" + "|" + row[16] + "|" + row[17] + "|" + row[18] + "|" + row[19] + "|" + row[20] + "|" + row[21] + "|" + row[22])
                if(User.objects.filter(username=row[cust_id]).exists()):         #checking if django user already exists
                    print("user(" + row[cust_id] + ")  to add already exists")
                else:
                    user = User.objects.create_user(row[cust_id], '', 'password')#otherwise creates the django user (this automatically creates an empty customer entry, linked with django user)
                user = User.objects.get(username=row[cust_id])       #all these row commands are just different columns of the .csv
                #obj1, created1 = Customers.objects.get_or_create(
                #    customer_id = user,
                user.customers.customer_name = row[cust_name]
                user.customers.customer_phone = row[cust_phone]
                user.customers.customer_address = row[cust_address]
                user.customers.customer_birthday = datetime.datetime.strptime(row[cust_birthday],'%d/%m/%Y').strftime('%Y-%m-%d')
                user.customers.customer_occupation = row[cust_occupation]
                user.customers.customer_gender = row[cust_gender]
                #)
                user.save()             #This automatically saves the customer part of the model
                obj1 = user.customers   #obj1 is now a customer object (you can just do obj1.customer_name = blah etc)

                # Adding Cars
                msg = "Now adding: |"
                for x in range(cr_id, cr_wheelbase + 1):
                    msg = msg + row[x] + "|"
                #print(msg)

                if(row[cr_seriesyear] == "NULL"):
                    row[cr_seriesyear] = "0"

                if(row[cr_pricenew] == "NULL"):
                    row[cr_pricenew] = "0"

                if(row[cr_seating] == "NULL"):
                    row[cr_seating] = "0"
                #If the car already exists, obj2 becomes a reference to the car. Otherwise, the car is created then a reference is passed to it.
                obj2, created2 = Cars.objects.get_or_create(
                    car_id = row[cr_id],
                    car_make = row[cr_make],
                    car_model = row[cr_model],
                    car_series = row[cr_series],
                    car_seriesyear = row[cr_seriesyear],
                    car_pricenew = row[cr_pricenew],
                    car_enginesize = row[cr_enginesize],
                    car_fuelsystem = row[cr_fuelsystem], 
                    car_tankcapacity = row[cr_tank],
                    car_power = row[cr_power],
                    car_seatingcapacity = row[cr_seating],
                    car_standardtransmission = row[cr_standardtransmission],
                    car_bodytype = row[cr_body],
                    car_drive = row[cr_drive],
                    car_wheelbase = row[cr_wheelbase]
                )
                obj2.save() #Saves car to the database
                #Adding Stores (pickup)
                msg = "Now adding(pickup): |"
                for x in range(3, 9):
                    msg = msg + row[x] + "|"
                #print(msg)
                obj3, created3 = Stores.objects.get_or_create(
                    store_id = row[3],
                    store_name = row[4],
                    store_address = row[5],
                    store_phone = row[6],
                    store_city = row[7],
                    store_state = row[8],
                )
                obj3.save()

                # Adding Stores (return)
                msg = "Now adding(return): |"
                for x in range(10, 16):
                    msg = msg + row[x] + "|"
                #print(msg)
                obj4, created4 = Stores.objects.get_or_create(
                    store_id = row[10],
                    store_name = row[11],
                    store_address = row[12],
                    store_phone = row[13],
                    store_city = row[14],
                    store_state = row[15],
                )
                obj4.save()
                
                # Adding Orders
                msg = "Now adding: |"
                for x in range(0, 4):
                    msg = msg + row[x] + "|"
                msg = msg + row[9] + "|"
                msg = msg + row[10] + "|"
                msg = msg + row[16] + "|"
                msg = msg + row[23] + "|"
                #print(msg)
                #The orders are done last, as they require the previous objects to have a foreign key reference to.
                obj5, created5 = Orders.objects.get_or_create(
                    order_id = row[0],
                    order_createdate = datetime.datetime.strptime(row[1],'%Y%m%d').strftime('%Y-%m-%d'),    #Converts the dates in the CSV file to the ones accepted by the database model.
                    order_pickupdate = datetime.datetime.strptime(row[2],'%Y%m%d').strftime('%Y-%m-%d'),
                    order_pickupstore = obj3,
                    order_returndate = datetime.datetime.strptime(row[9],'%Y%m%d').strftime('%Y-%m-%d'),
                    order_returnstore = obj4,
                    order_customer = obj1,
                    order_car = obj2
                )
                obj5.save()
                

            a += 1  #counter used just so the first column isn't added.
        
        
