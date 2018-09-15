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
def importthedata():      
    with open('data.csv', newline='') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')       
        a = 0
        for row in datareader:   
            if(a > 0):
                
                exists = False
                if Customers.objects.filter(customer_id=row[16]).exists():
                    exists = True
                if(not exists):
                    print("Now adding:" + "|" + row[16] + "|" + row[17] + "|" + row[18] + "|" + row[19] + "|" + row[20] + "|" + row[21] + "|" + row[22])
                    obj= Customers(
                        customer_id = row[16],
                        customer_name = row[17],
                        customer_phone = row[18],
                        customer_address = row[19],
                        customer_birthday = datetime.datetime.strptime(row[20],'%d/%m/%Y').strftime('%Y-%m-%d'),
                        customer_occupation = row[21],
                        customer_gender = row[22]
                    )
                    obj.save()
                    
                
            a += 1
        
        
