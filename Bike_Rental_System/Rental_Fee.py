"""
Rent bikes on hourly basis $5 per hour.
Rent bikes on daily basis $20 per day.
Rent bikes on weekly basis $60 per week.
"""

from abc import ABC, abstractmethod
from Bike_Order import Order
from datetime import datetime

class RentalFee(ABC):

    @abstractmethod
    def calculate_fee(self) -> int :
        pass
    
    def current_rental_duration(self, order) -> datetime:
        return datetime.now()- order.get_order_date()
        #duration rented #format: days,hours:minutes:seconds.microseconds

class NoDiscountRentalFee(RentalFee): 


    def calculate_fee(self, order) -> int:
        bill = 0
        rental_duration = super().current_rental_duration(order) 
        days = rental_duration.days
        
        #if less than 7days add the days to bill
        #if greater than 7days add the week(s) and days to bill
        #if exactly a week just add the week to the bill
        bill = days * 20 if days < 7 else ( (days % 7) * 20 + (days // 7) * 60 if days > 7 else 60 ) 
                  
        #bill += rental_duration.hour * 5 #hourly
        
        return bill

class FamilyDiscountRentalFee(RentalFee):

     def calculate_fee(self, order)-> int:
        bill = 0
        rental_duration = super().current_rental_duration(order)
        print(rental_duration)

        #calculate weeks/months/years/rental 
        days = rental_duration.days
        bill = days * 20 if days < 7 else ( (days % 7) * 20 + (days // 7) * 60 if days > 7 else 60 ) 
        
        #calculate hours
        #bill += rental_duration.hour * 5 #hourly
        
        bill *= 0.7 #family discount 30% off
        
        return bill

        

        
