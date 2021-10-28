from datetime import datetime


class Order:
    
    def __init__(self):
        self.order_date =  datetime(2020,10,20,5,1,25,831269) #datetime.now()
        self.name = ""
        self.telephone = ""
        self.address = ""
        self.order_status = False
        print("Order date start:", self.order_date)
    
    def place_order(self, bikes_ordered) -> bool:
        #bikes_ordered
        #cross check with inventory 
        #if bikes_ordered <=  Inventory.GetBikeQuantity: self.order_status = True
    
        return self.order_status
    
    def set_order_details(self, name, tele, address):
        self.name = name
        self.telephone = tele
        self.address = address

    def get_order_status(self) -> bool:
        print("Order Active: ", self.order_status)
        return self.order_status

    def get_order_date(self) -> datetime:
        return self.order_date
        

    


        
