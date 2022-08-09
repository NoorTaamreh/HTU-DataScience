class ReleaseDate:
    def __init__(self, year):
        self.year=year

class Vehicle:
    L1=[]
    def __init__(self,id,country,priceRange,year):
        self.__id=id
        self.__country=country
        self.__priceRange=priceRange
        self.__purDate=ReleaseDate(year)
        

        

    def setCountry(self,country):
        self.__country=country

    def getCountry(self):
        return self.__country    

        
    def checkLuxury(self):
        L1=[]
        if self.__priceRange > 30000:
            L1.append(self.__id)
        return L1


class Ford(Vehicle):
    def __init__(self, id, country, priceRange, year,type):
        super().__init__(id, country, priceRange, year)
        self.type=type

    def getType(self):
        print(self.type)


V1=Vehicle(1,'Germany',40000,2022)
print(V1.getCountry())
List1=V1.checkLuxury()
print(List1)

V2=Ford(2,'USA',15000,2016,'electric')
V2.getType()





