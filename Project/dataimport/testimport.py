#Reference for the position of objects within the data.csv
'''
0 = Order_ID
1 = Order_CreateDate
2 = Order_PickupDate
3 = Order_PickupStore
4 = Pickup_Store_Name
5 = Pickup_Store_Address
6 = Pickup_Store_Phone
7 = Pickup_Store_City
8 = Pickup_Store_State_Name
9 = Order_ReturnDate
10 = Order_ReturnStore
11 = Return_Store_Name
12 = Return_Store_Address
13 = Return_Store_Phone
14 = Return_Store_City
15 = Return_Store_State
16 = Customer_ID
17 = Customer_Name
18 = Customer_Phone
19 = Customer_Addresss
20 = Customer_Brithday
21 = Customer_Occupation
22 = Customer_Gender
23 = Car_ID
24 = Car_MakeName
25 = Car_Model
26 = Car_Series
27 = Car_SeriesYear
28 = Car_PriceNew
29 = Car_EngineSize
30 = Car_FuelSystem
31 = Car_TankCapacity
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
def importthedata():      
    with open('data.csv', newline='') as csvfile:   #Opens the CSV file , with delimiter ','
        datareader = csv.reader(csvfile, delimiter=',')       
        a = 0
        for row in datareader:   #Iterates through every row in the CSV file 
            if(a > 0):  #Ignores the first row, as it contains the heading for the data
                # Adding Customers  
                #print("Now adding:" + "|" + row[16] + "|" + row[17] + "|" + row[18] + "|" + row[19] + "|" + row[20] + "|" + row[21] + "|" + row[22])
                if(User.objects.filter(username=row[16]).exists()):         #checking if django user already exists
                    print("user(" + row[16] + ")  to add already exists")
                else:
                    user = User.objects.create_user(row[16], '', 'password')#otherwise creates the django user (this automatically creates an empty customer entry, linked with django user)
                user = User.objects.get(username=row[16])       #all these row commands are just different columns of the .csv
                #obj1, created1 = Customers.objects.get_or_create(
                #    customer_id = user,
                user.customers.customer_name = row[17]
                user.customers.customer_phone = row[18]
                user.customers.customer_address = row[19]
                user.customers.customer_birthday = datetime.datetime.strptime(row[20],'%d/%m/%Y').strftime('%Y-%m-%d')
                user.customers.customer_occupation = row[21]
                user.customers.customer_gender = row[22]
                #)
                user.save()             #This automatically saves the customer part of the model
                obj1 = user.customers   #obj1 is now a customer object (you can just do obj1.customer_name = blah etc)

                # Adding Cars
                msg = "Now adding: |"
                for x in range(23, 38):
                    msg = msg + row[x] + "|"
                #print(msg)

                if(row[27] == "NULL"):
                    row[27] = "0"

                if(row[28] == "NULL"):
                    row[28] = "0"

                if(row[33] == "NULL"):
                    row[33] = "0"
                #If the car already exists, obj2 becomes a reference to the car. Otherwise, the car is created then a reference is passed to it.
                obj2, created2 = Cars.objects.get_or_create(
                    car_id = row[23],
                    car_make = row[24],
                    car_model = row[25],
                    car_series = row[26],
                    car_seriesyear = row[27],
                    car_pricenew = row[28],
                    car_enginesize = row[29],
                    car_fuelsystem = row[30], 
                    car_tankcapacity = row[31],
                    car_power = row[32],
                    car_seatingcapacity = row[33],
                    car_standardtransmission = row[34],
                    car_bodytype = row[35],
                    car_drive = row[36],
                    car_wheelbase = row[37]
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
        
        
