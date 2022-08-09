class Employee:
    raise_amount = 1.1 
    
    def __init__(self, firstname, lastname, email, salary):
        #these are called attributes to a class
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.salary = salary
    def get_info(self):
        print(self.firstname, self.lastname, self.email)


employee1=Employee("ahmad","4","4")
print(employee1)