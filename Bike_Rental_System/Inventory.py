class InventorySingleton(object):
  def __new__(cls): #static method #cls class to be instaniated 
    if not hasattr(cls, 'instance'):
      cls.instance = super(InventorySingleton, cls).__new__(cls) #creates the object if it does not exist 
    return cls.instance
    def __init__(self):
        self.quantity_of_bikes = 20

    def get_quantity_of_bikes(self):
        print("Quantity of bikes", self.quantity_of_bikes)
        return self.quantity_of_bikes
