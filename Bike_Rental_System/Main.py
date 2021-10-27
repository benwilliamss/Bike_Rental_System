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
import Bike_Rental

def main():

    #have the user interface here 

    #call the bike rental system as soon as 

    standing_account = Bike_Rental.BikeRentalFee()
    #standing_account.rental_duration()

    print("Amount to pay £",standing_account.calculate_rental_fee(False))
    

main()