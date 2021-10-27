from datetime import datetime
"""
Rent bikes on hourly basis $5 per hour.
Rent bikes on daily basis $20 per day.
Rent bikes on weekly basis $60 per week.
"""

class BikeRentalFee: 
   
    def __init__(self):
        self.rental_start = datetime(2020,10,20,5,1,25,831269) #datetime.now()
        self.bill = 0
        print("Rental started on:  ", self.rental_start)

    def calculate_rental_fee(self, family_promotion):
        rental_duration = datetime.now()-self.rental_start #duration rented #format: days,hours:minutes:seconds.microseconds
       
        days = rental_duration.days
        

        #if less than 7days add the days to bill
        #if greater than 7days add the week(s) and days to bill
        #if exactly a week just add the week to the bill
        self.bill = days * 20 if days < 7 else ( (days % 7) * 20 + (days // 7) * 60 if days > 7 else 60 ) 
                  
        self.bill += rental_duration.hour * 5 #hourly
        
        if(family_promotion): self.bill *= 0.7 #family discount 30%
        
        return self.bill

    def rental_duration(self):
       duration = datetime.now() - self.rental_start
       #print(duration)
       #day = duration.strftime("%d")
       #print(day)
       print(duration.hours)
    

        
