from datetime import datetime


class Order:
    
    def __init__(self):
        self.order_date =  datetime(2020,10,20,5,1,25,831269) #datetime.now()
        print("Order date start:", self.order_date)
    
    def place_order(self, bikes_ordered):
        #bikes_ordered
        Order_Confirmed()
        
    def current_rental_duration(self) -> datetime:
        return (datetime.now()-self.order_date) #duration rented #format: days,hours:minutes:seconds.microseconds
        

    def Order_Confirmed(self) -> bool:
        # needs to cross cross reference stock 
        return true


        
