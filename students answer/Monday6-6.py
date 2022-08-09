import time

class Dateofpurchase():
     def __init__(self):
        self.release = time.asctime()
    
      

class Vechiles():
    def __init__(self, vechile_number, country, model):
        self.__model = model
        self.__originofcountry = country
        self.__numberno = vechile_number 
        self.__dateofpurchase= Dateofpurchase()  #composition 
    def getmodel(self):                            #getter for private instances 
        return (self.__model)
    def getorigin(self):
        return (self.__originofcountry)
    def getnumb(self):
        return (self.__numberno)
    def getdate(self):
        return(self.__dateofpurchase.release)
    def setmodel(self, type):                      #setters for private instances
        self.__model = type
    def setnumber(self, number):
        self.__numberno = number
    def setdate(self):
        self.__dateofpurchase = Dateofpurchase()
    
    def governante(self):                       #regular method to identify Vechile governante based on it number(suppose that has 5 digit numbers)
        x = self.__numberno // 1000
        if x == 12:
            return 'amman'
        if x == 24:
            return 'southgover'
        if x == 25:
            return 'north gover'
#child class
class Cars(Vechiles):    #inheritance 
    Engine_Capcities = []
    # Countries = {}
    def __init__(self, vechile_number, country, model, motortype, enginecapacity):
        super().__init__(vechile_number, country, model)
        self.__motortype = motortype
        self.__enginecapacity= enginecapacity
        self.__insertdate= Dateofpurchase()
    #getters of private instances
    def getmotortype(self):
        return self.__motortype
    def getcap (self):
        return self.__enginecapacity
    def getdate (self):                  #this getter has the same name as getter in the parent class,return different argunment 
        return self.__insertdate.release
    def addcapcities (self):             #this is regular method to accumalitive all capacities of car objects
       Cars.Engine_Capcities.append (self.__enginecapacity)
    # def addcountry (self):               #this is regular method to add country to the car country list with indexed
    #     g = int(self.getnumb()// 1000)
    #     coun = [self.getorigin(), g]
    #     Cars.Countries.update (coun)
    # def coun_based_gov(self):  #this is regular method to find countries of cars in specfic governante
    #     y =self.getnumb()// 1000
        

        

v1 = Vechiles(12345, 'Jordan', 306030)
print(v1.getdate(), v1.governante())
time.sleep(2)
v1.setdate()
print(v1.getdate())
C1 = Cars(14555, 'Saudi', 306030, 'Hyprid', 2500)
print(C1.getdate())
print(C1.getcap())
C1.addcapcities()
print(C1.Engine_Capcities)







        



























# class warehouse:
#     def __init__(self, capacity, location, annualrent, manger_name):
#         self.capacity = capacity
#         self.location = location
#         self.annualrent = annualrent
#         self.manager_name= manger_name
#         self.__Categories = 'Default'
#         self.Id =self.__setterId(location, manger_name)
#     def getcat (self):
#         return self.__Categories
#     def setcat (self, cat1):
#         self.__Categories = cat1
#     def __setterId (self, location, manger_name):
#         Id = location+ manger_name 
#         return Id

# Store1 = warehouse(100,'amman','700','Moh')
# print(Store1.getcat())
# Store1.setcat('Car')
# print(Store1.getcat())
# print(Store1.Id)

#     # def get_mangername(self):
#     #     print(self.manager_name)
#     # def changerent (self, newrent):
#     #     self.annualrent = newrent
    
# # class Cars(warehouse):
# #     def __init__(self, capacity, location, annualrent, manger_name, carmodel, carnumber):
# #         super().__init__(capacity, location, annualrent, manger_name)
# #         self.carmodel = carmodel
# #         self.carnumber = carnumber
# #     def output (self):
# #         print(self.carmodel)
# #     def changerent (self, newrent):
# #         self.annualrent = newrent