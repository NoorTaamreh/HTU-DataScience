#OOP

#1
from cgi import print_form


class fruit:
    def __init__(self):
        self.name="Apple"
        self.color="Red"

my_fruit= fruit()
# print(my_fruit.name)

#2
my_fruit.color="green"
my_fruit.name="Kiwi"
print(my_fruit.name)
print(my_fruit.color)


#3
# class fruit2:
#     def __in1t__(self,name,color):
#         self.name=name
#         self.color=color
# # Apple=fruit2()     
# Apple=fruit2('Apple','Red')
# Kiwi=fruit2('Kiwi',"Green")
# print('test',Apple.name)

#4
# class fruit2:
#     def __init__(self,name,color):
#         self.name= name
#         self.color= color
            
#     def details(self):
#         print("My"+self.name+"is"+self.color)

# apple= fruit2("Apple","Red")
# apple.details()

#5
#-----------------------------------------------------------------
# from Car import Car
# car_1 = Car("Chevy","Corvette",2021,"blue")
# car_2 = Car("Ford","Mustang",2022,"red")

# car_1.drive()
# car_2.stop()
#-----------------------------------------------------------------
class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive1(self):
        print("This car is driving")

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")
        

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_1.year)
car_1.drive1()

car_1.drive()
car_2.stop()
#----------------------------------------------------------------

#6
# class Guitar:
#     def __init__(self):
#         self.string= 6
#         self.play()
     
#     def play(self):
#         print("TT Tra ")
   
# MyGuitar=Guitar()
# print(MyGuitar.string)

class Guitar:
    def __init__(self,color):
        self.color="Black"
        self.play()
     
    def play(self):
        print("tt tra ")
   
MyGuitar=Guitar("Brown")
print(MyGuitar.color)  #BROWN
MyGuitar.play()    #tt tra 

#inhirtance
class ElectricGutar(Guitar):
    pass # take all the attribuites and the function in the parent class 

MyGuitar2=ElectricGutar()
print(MyGuitar2.color) #you'll pass the attribuitr and the function in the class
#Black

class OldGutar(Guitar):
    def Loud(self):
        print("tt tra ".upper())
        
MyGuitar3=OldGutar()
print(MyGuitar3.Loud)  #TT TRA
MyGuitar3.loud()   #TT TRA
#---------------

class OldGutar(Guitar):
    def __init__(self):
        super().__int__()
        self.color="Red" #to replace the value in the main class    
        # self.__cost=100 #privte attribute    
    def Loud(self):
        print("tt tra ".upper())
        

print("Parent class",Guitar().color)
print("child class",OldGutar().color)
MyGuitar3=OldGutar()

#to accsess to the value of the privite attribute
#print(MyGuitar3._OldGuitar__cost)
#if the privte attribute in the parent class and not in the child class we can accsess it
#Object._parentclass__attribute
#print(MyGuitar3._Guitar__cost)
#--------------

#privte method
def __secret(self):
    print('This is privte method')
MyGuitar3._OldGuitar__secret()

#call privte method   

#you can set defulte value for the paramter