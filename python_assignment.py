import numpy as np
import pandas as pd
class flights:
    data={'Flight_id':['AI161E90','BR161F91','AI161F99','VS171E20','AS171G30','AI131F49'],
          'From':['BLR','BOM','BBI','JLR','HYD','HYD'],
          'To':['BOM','BBI','BLR','BBI','JLR','BOM'],
          'Price':[5600,6750,8210,5500,4400,3499]}
    database = pd.DataFrame(data)
    def from_name(self,name):
        print(self.database[(self.database['From']==name)|(self.database['To']==name)])
    def from_city(self,city):
        print(self.database[(self.database['From']==city)])
    def from_multiple_city(self,city1,city2):
        print(self.database[(self.database['From']==city1)&(self.database['To']==city2)])

def main():
    f=flights()
    city_names={'BLR': 'Bengaluru', 'BOM': "Mumbai", 'BBI': 'Bhubaneswar', 'HYD': 'Hyderabad', 'JLR': 'Jabalpur'}
    print("Welcome to the Flight Booking System")
    print("1. Flights for a particular City\n2. Flights From a city\n3. Flights between two given cities")
    i=int(input("Enter your choice: "))
    if(i==1):
        c=input("Which city do you want flight details of? : ")
        c.lower()
        for key,value in city_names.items():
            if ((key.lower()==c) |(value.lower()==c)):
                f.from_name(key)
            else:
                pass
    elif(i==2):
        c=input("From which city do you want flight details of? : ")
        c.lower()
        for key,value in city_names.items():
            if ((key.lower()==c) |(value.lower()==c)):
                f.from_city(key)
            else:
                pass
    elif(i==3):
        a=input("Enter initial city: ").lower()
        b=input("Enter final city: ").lower()
        key1=""
        key2=""
        for key,value in city_names.items():
            if ((key.lower()==a) |(value.lower()==a)):
                key1=key
            else:
                pass
            if ((key.lower()==b) |(value.lower()==b)):
                key2=key
            else:
                pass
        f.from_multiple_city(key1,key2)
main()
