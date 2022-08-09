class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def get_date(self):
        ddmmyy = f"{self.day} {self.month} {self.year}"
        return ddmmyy

class Warehouse:
    def __init__(self, warehouse_name,storage_capacity, manager, annual_rent, location):
        self.warehouse_name = warehouse_name
        self.storage_capacity = storage_capacity
        self.manager = manager
        self.__annual_rent = annual_rent
        self.location = location
    def __info__(self):
        return f'Storage Capacity : {self.storage_capacity}\nManager : {self.manager}\nAnnual Rent : {self.annual_rent}\nLocation : {self.location}'
    def __expand_storage_capacity(self, new_capacity):
        "used to add new storage capacity to the warehouse"
        self.storage_capacity = new_capacity

    def set_rent(self, newrent):
        self.__annual_rent = newrent

    def get_rent(self):
        return self.__annual_rent
    def set_storage_cap(self, newvalue):
        self.__expand_storage_capacity(newvalue)
    
    @classmethod
    def from_string(cls, string):
        storage_capacity, manager, annual_rent, location = string.split(" ")
        return cls(storage_capacity, manager, annual_rent, location)
    

class Product(Warehouse):
    """products class supposed to manage the the product code and name and define the production and expiration date"""
    def __init__(self, storage_capacity, manager, annual_rent, location, product_code, product_name, pday, pmonth, pyear, eday, emonth, eyear):
        super().__init__(storage_capacity, manager, annual_rent, location)
        self.product_code = product_code
        self.product_name = product_name
        self.production_date = Date(pday, pmonth, pyear)
        self.expiry_date = Date(eday, emonth, eyear)
    def __info__(self):
        return f'Storage Capacity : {self.storage_capacity}\nManager : {self.manager}\nAnnual Rent : {self.annual_rent}\nLocation : {self.location}\nProduction Date : {self.production_date.get_date()}\nExpiration Date : {self.expiry_date.get_date()} '

class Employee(Warehouse):
    base_payment = 350
    def __init__(self, storage_capacity, manager, annual_rent, location, emp_name, emp_phone, emp_salary, hday, hmonth, hyear):
        super().__init__(storage_capacity, manager, annual_rent, location)
        self.name = emp_name
        self.phone = emp_phone
        self.salary = emp_salary
        self.hiring_date = Date(hday, hmonth, hyear)

    def __info__(self):
        return f'Storage Capacity : {self.storage_capacity}\nManager : {self.manager}\nAnnual Rent : {self.annual_rent}\nLocation : {self.location}\nHiring Date : {self.hiring_date.get_date()} '    

    @classmethod
    def from_string(cls, string):
        storage_capacity, manager, annual_rent, location, emp_name, emp_phone, emp_salary, hday, hmonth, hyear = string.split(" ")
        return cls(storage_capacity, manager, annual_rent, location, emp_name, emp_phone, emp_salary, hday, hmonth, hyear)

    @classmethod
    def raise_base_payment(cls, payment):
        cls.base_payment = payment



warehouse1 = Warehouse("SafeHouse", 2000, "Tamer Hussien", 900, "Balqaa, Ain EL Basha")
print(warehouse1.get_rent())
print(warehouse1.storage_capacity) # call the old storage capacity
warehouse1.set_storage_cap(3000) # set new value to storage capacity using private method
print(warehouse1.storage_capacity) # call the new value of storage capacity