"""
A Bike Rental System

A full fledged bike rental system implemented in Python using object oriented programming.
Customers can

    See available bikes on the shop
    Rent bikes on hourly basis $5 per hour.
    Rent bikes on daily basis $20 per day.
    Rent bikes on weekly basis $60 per week.
    Family Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price

The bike rental shop can

    issue a bill when customer decides to return the bike.
    display available inventory
    take requests on hourly, daily and weekly basis by cross verifying stock
  """
import Rental_Fee
from Bike_Order import Order

def main():

    #have the user interface here 

    #call the bike rental system as soon as 
    family_order = Order()

    solo_order = Order()
    
    individual_account_fee = Rental_Fee.NoDiscountRentalFee()
    family_account_fee = Rental_Fee.FamilyDiscountRentalFee()
    #standing_account.rental_duration()

    print("Amount the family has to pay £", family_account_fee.calculate_fee(family_order))
    print("Amount the individual has to pay £",individual_account_fee.calculate_fee(solo_order)) 
    

main()