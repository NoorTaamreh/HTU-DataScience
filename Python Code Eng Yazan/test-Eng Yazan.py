class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    


class Employee:
    #Class Instance can be accessed through instance itself or class 
    raise_amount = 1.1
    
    #This is the initializer function it is used to initialize values of the object we create
    #self refers to the object that called the class
    def __init__(self, firstname, lastname, email, salary): # day , month , year):
        #these are called attributes to a class
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.salary = salary
        #self.hiring_date = Date(day, month, year)
        #self.__id = 20
    
    #this is a regular method (all functions in classes are called methods)
    def fullname(self):
        return '{} {}'.format(self.firstname , self.lastname)

    def test(self, param = None):
        return param

    def test(self):
        return 5
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, inputstring):
        firstname , lastname , email, salary = inputstring.split(" ")
        return cls(firstname, lastname, email, salary)

    @staticmethod
    def workday(day):
        if day == 5 or day == 6:
            return False
        return True
    

employee1 = Employee.from_string('ahmad moh a@gmail.com 1000')

x = employee1.test()
print(x)


class Developer(Employee):
    #raise_amount = 1.2

    def __init__(self, firstname, lastname, email, salary, proglanguage):
        super().__init__(firstname, lastname, email, salary)
        self.proglanguage = proglanguage

    def fullname(self):
        return 'this is the fullname of developer class'

dev1 = Developer('tariq', 'ahmad', '@hotmail.com', 2000, 'Python')


# print(employee1.__id)



