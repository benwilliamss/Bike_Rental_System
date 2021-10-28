"""
Rent bikes on hourly basis $5 per hour.
Rent bikes on daily basis $20 per day.
Rent bikes on weekly basis $60 per week.
"""

from abc import ABC, abstractmethod
from Bike_Order import Order


class RentalFee(ABC):

    @abstractmethod
    def calculate_fee(self) -> int :
        pass
    
    


class NoDiscountRentalFee(RentalFee): 


    def calculate_fee(self, Order):
        bill = 0
        rental_duration = Order.current_rental_duration() #composition to avoid further dependentcies with inheritance
        days = rental_duration.days
        
        #if less than 7days add the days to bill
        #if greater than 7days add the week(s) and days to bill
        #if exactly a week just add the week to the bill
        bill = days * 20 if days < 7 else ( (days % 7) * 20 + (days // 7) * 60 if days > 7 else 60 ) 
                  
        #bill += rental_duration.hour * 5 #hourly
        
        return bill

class FamilyDiscountRentalFee(RentalFee):

     def calculate_fee(self, Order):
        bill = 0
        rental_duration = Order.current_rental_duration()
        print(rental_duration)

        #calculate weeks/months/years/rental 
        days = rental_duration.days
        bill = days * 20 if days < 7 else ( (days % 7) * 20 + (days // 7) * 60 if days > 7 else 60 ) 
        
        #calculate hours
        #bill += rental_duration.hour * 5 #hourly
        
        bill *= 0.7 #family discount 30% off
        
        return bill

        

        
