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
from Inventory import InventorySingleton

def main():

    #initialise inventory and potentially 

    BikeInventory = InventorySingleton() #inventory

    #while loop - undefined amount of iterations
    #Two options: Order a bike or pay and return
     
#have the user interface here 
    #order a bike 
    """
    - will create an object for order containing user details 
     -user details will need to be checked for string types on tele, name and address
    """
    #pay & return
    """
    - will need to fetch object of the 
    - will call the rental fee 
    - will delete the object of rental fee after paid??
    - bikes returned will need to update the inventory
    """ 

    

    #call the bike rental system as soon as 
    family_order = Order()

    solo_order = Order() #move Order() that into the condition below 

    #solo_order.set_order_details("Ben Williams","0730283048", "34 Zoo Lane, Powys, Wales") if solo_order.place_order(1) else print("order failed. Please select a new option") 
    
    individual_account_fee = Rental_Fee.NoDiscountRentalFee()
    family_account_fee = Rental_Fee.FamilyDiscountRentalFee()
    #standing_account.rental_duration()

    print("Amount the family has to pay £", family_account_fee.calculate_fee(family_order))
    print("Amount the individual has to pay £",individual_account_fee.calculate_fee(solo_order)) 
    

main()