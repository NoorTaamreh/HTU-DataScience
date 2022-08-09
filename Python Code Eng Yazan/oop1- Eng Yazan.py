class Employee:
    #Class Instance can be accessed through instance itself or class 
    raise_amount = 1.1
    
    #This is the initializer function it is used to initialize values of the object we create
    #self refers to the object that called the class
    def __init__(self, firstname, lastname, email, salary):
        #these are called attributes to a class
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.salary = salary
    
    #this is a regular method (all functions in classes are called methods)
    def fullname(self):
        return '{} {}'.format(self.firstname , self.lastname)
    


#here we created two instances from one class
employee1 = Employee('ahmad moh a@gmail.com 1000')
employee2 = Employee('hazim', 'zaid', 'b@yahoo.com', 2000)

#this is used to print out the instance variables for an instance of out choosing
print(employee1.__dict__)


#You can access the class variable through the instance itself or the class like the follwing

print(employee1.raise_amount)
print(Employee.raise_amount)