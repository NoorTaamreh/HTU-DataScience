class Date:
     
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def Epoch(self):
        return 5
 
class Employee:
    #if you want to leave it empty put pass statement.
    #pass
    
    #this a class variable
    raise_amount = 1.1
    num_employees = 0
 
    def __init__(self, firstname , lastname, email, salary, day , month , year):
        #these are called attributes to a class
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.salary = salary
        self.hiring_date = Date(day, month, year) # composition
 
#inheritance 

class Developer(Employee):
    raise_amount = 1.2
 
    def __init__(self, firstname, lastname, email, salary, proglanguage):
        super().__init__(firstname, lastname, email, salary)
        self.proglanguage = proglanguage