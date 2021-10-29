class InventorySingleton(object):

    """ Singleton have one instance at all time 
        This is a class dedicated to storing the bike quantity for the store
    """
    def __new__(cls): #static method #cls class to be instaniated 
        if not hasattr(cls, 'instance'):
          cls.instance = super(InventorySingleton, cls).__new__(cls) #creates the object if it does not exist 
        return cls.instance
    
    def __init__(self):
        self.quantity_of_bikes = 20

    def get_quantity_of_bikes(self) -> int:
        print("Quantity of bikes", self.quantity_of_bikes)
        return self.quantity_of_bikes
