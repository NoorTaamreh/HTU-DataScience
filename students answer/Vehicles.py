class Release_data:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    
         
class Vehicles :
     l=list()

     def __init__ (self, major ,quntty ,contry, day , month , year):
        self.__major= major
        self.__quntty= quntty
        self.__contry=contry
        self.release_data = Release_data(day, month, year)
    
     def get_info(self ):
        return  ( 'type: {} qunnttey= {} contry {}: release_data is : {}/ {} / {}'.format(self.__major , self.__quntty ,self.__contry, self.release_data.day ,self.release_data.month ,self.release_data.year))

     def set_info( self,major ,quntty ,contry, day , month , year ):
         
         self.__major= major
         self.__quntty=quntty   #q of major type 
         self.day=day
         self.month=month
         self.year=year
         self.__contry=contry

     def numofvins (self ,tn ,q ,l ):
         
         Vehicles.l.append(tn)
         Vehicles.l.append(q)
         if tn.lower()== "cars":
             return q
         print(l)
     
         
         


class  Cars (Vehicles ):
    def __init__ (self, name ,pric ,quntty1 ,modle  ):
        self.__name=name
        self.__pric=pric
        self.__quntty1=quntty1 
        self.__modle=modle
        

    def set_info(self, name ,npric ,nquntty ,nmodle ):

         self.__name= name
         self.__quntty1=nquntty
         self.__modle=nmodle 
         self.__pric=npric
         
         

    def get_info(self ):
          
        return 'type  of car {}  remain quntty is{}  the modle is{} price of car   {} '.format(self.__name,self.__quntty1,self.__modle , self.__pric) 

    
    
    def purchaserequest (self , name,qr ,modle  ):
        self.__quntty1= self.__quntty1-qr
        
        print ('I want to buy cars {}'.format(qr))
        print ('Total price {}'.format(self.__pric*qr))

        print('Remain quntty is {} Type of of car {} The modle is   {}  '.format(self.__quntty1, self.__name  ,self.__modle))
         
    
    
  

o= Vehicles( "cars" ,50 ,"amerca" ,1,1,2220)
o. numofvins("cars", 300 ,Vehicles.l)
o. numofvins("trucK",100,Vehicles.l)

o2=Cars("BMW", 20000, 20, "2010")

print (o.get_info())
o.set_info("truks" ,50,"jordan ",1,12,2022)
print (o.get_info())
print(o2.get_info())
o2.purchaserequest("bm", 2, "210")





# o2.set_info( "bm", 1000, 55555, "nmodle")
# o2.purchaserequest("bm",15,"2010")    

# init
# 30
# sub class 2 (another type of vehicle)
# init
# parent initializer, you can use if you want
# class release_data
# init
# class vehicles
# init countries
# sub class 1 (type of vehicle)
# init
# 30
# sub class 2 (another type of vehicle)
# init
# parent initializer, you can use if you want
# all private, setters , getters, all classes sub and main
# parent , list sub categories europe asia america
# sub classes 1 method of your choosing not print or change
# type how much left in the store
# purchase request 29