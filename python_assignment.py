import numpy as np
import pandas as pd

class Flights:
    data = {'Flight_id': ['AI161E90', 'BR161F91', 'AI161F99', 'VS171E20', 'AS171G30', 'AI131F49'],
            'From': ['BLR', 'BOM', 'BBI', 'JLR', 'HYD', 'HYD'],
            'To': ['BOM', 'BBI', 'BLR', 'BBI', 'JLR', 'BOM'],
            'Price': [5600, 6750, 8210, 5500, 4400, 3499]}
    database = pd.DataFrame(data)
    
    def from_name(self, name):
        print(self.database[(self.database['From'] == name) | (self.database['To'] == name)])
        
    def from_city(self, city):
        print(self.database[(self.database['From'] == city)])
        
    def from_multiple_city(self, city1, city2):
        print(self.database[(self.database['From'] == city1) & (self.database['To'] == city2)])

def main():
    f = Flights()
    city_names = {'BLR': 'Bengaluru', 'BOM': 'Mumbai', 'BBI': 'Bhubaneswar', 'HYD': 'Hyderabad', 'JLR': 'Jabalpur'}
    
    print("Welcome to the Flight Booking System")
    
    while True:
        print("\n1. Flights for a particular City\n2. Flights From a city\n3. Flights between two given cities")
        
        i = int(input("Enter your choice: "))
        
        if i == 1:
            while True:
                c = input("Which city do you want flight details of? : ").upper()
                if c in city_names:
                    f.from_name(c)
                    break
                else:
                    print("Invalid city name. Please try again.")
                    
        elif i == 2:
            while True:
                c = input("From which city do you want flight details of? : ").upper()
                if c in city_names:
                    f.from_city(c)
                    break
                else:
                    print("Invalid city name. Please try again.")
                    
        elif i == 3:
            while True:
                a = input("Enter initial city: ").upper()
                b = input("Enter final city: ").upper()
                
                if a in city_names and b in city_names:
                    f.from_multiple_city(a, b)
                    break
                else:
                    print("Invalid city names. Please try again.")
        
        else:
            print("Invalid choice.")
        
        continue_search = input("\nDo you want to continue searching? (yes/no): ").lower()
        if continue_search != "yes":
            break

main()
