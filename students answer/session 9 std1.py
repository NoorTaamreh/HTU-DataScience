class Vehicals:
    
    def __init__(self, country, fuel_type, price):
        self.country = country
        self.fuel_type = fuel_type
        self.price = price
        self.list1 = []
 
    def info(self, info):
        if info > 15000:
            self.list1.append(info)

            
    def get_average_model(self):
        value = 0