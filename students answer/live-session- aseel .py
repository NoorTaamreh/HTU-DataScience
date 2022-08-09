import sqlite3
# #create database
# conn = sqlite3.connect('information_univarsity.db')
# cur = conn.cursor()
# table1 = ''' create table Employees(
#         SSN		char(9) 	not null,
# 	    Name 	varchar(20),
#         salary  number(20),
#         Major   varchar(30));'''
# table2  = '''create table Student( 
#         SSN		char(9) 	not null,
# 	    Name 	varchar(20),
# 		GPA 	number(3,2), 
# 	    Age 	number(2), 
#         Major   varchar(30),
#         year    number(4),
# 		primary key (SSN));
#         '''
# #foreign key (Major) REFERENCES Depatments(Name)
# cur.execute(table1)
# cur.execute(table2)
# conn.commit()
# conn.close()

class Majorr:
    def __init__(self, subj, chours =0):
        self.subj = subj
        self.chours = chours


# class Subject:
#     def __init__(self, Chours, typeas):
#         pass
class Student:
    
    def __init__(self, SSN, Name, Msubj, Age, years, GPA, time = 0):
        self.years= years
        self.Msubj = Majorr(Msubj)
        self.time = time
        self.Name = Name
        self.GPA = GPA
        self.SSN = SSN
        self.Age = Age
        conn = sqlite3.connect('information_univarsity.db')
        cur = conn.cursor()
        qinsert = f'insert into Student(SSN, Name, GPA, Age, Major) values ({self.Name}, {self.Msubj}, {self.years}, {self.GPA});'
        cur.execute(qinsert)
        conn.commit()
        conn.close()
    
    def Reg_year(self):
        if self. years == 4 :
            t = self.time = 1
            print("First Register" + t)
        
        elif self.years == 3:
            t = self.time = 2
            print("Seconed Register" + t)
        
        elif self.years == 2:
            t = self.time = 3
            print("Three Register" + t)

        elif self.years == 1:
            t = self.time = 4
            print("Fifth Register" + t)
        
        else:
            print( " A Register is avaliable after 4 hours")
    

    def set_student(self, nName, nMsubj, nyears, nGPA ):
        
        self.Name = nName
        self.Msubj = nMsubj
        self.years = nyears
        self.GPA = nGPA
        conn = sqlite3.connect('information_univarsity.db')
        cur = conn.cursor()
        qinsert1 = f'insert into Student(SSN, Name, GPA, Age, Major) values ({self.Name}, {self.Msubj}, {self.years}, {self.GPA});'
        cur.execute(qinsert1)
        conn.commit()
        conn.close()

class Employees:
    adhour = 20
    def __init__(self, SSN, Name, salary, course, addtion_salary = 0):
        self.salary = salary
        self.course = Majorr(course)
        self.addtion_salary = addtion_salary
        self.Name = Name
        self.SSN = SSN
        conn = sqlite3.connect('information_univarsity.db')
        cur = conn.cursor()
        qinsert3 = f'insert into Employees(SSN, Name, salary, Major) values({self.SSN}, {self.Name}, {self.salary}, {self.course});'
        cur.execute(qinsert3)
        conn.commit()
        conn.close()
    
    def addtion_hours(self, new_val):
        self.addtion_salary = new_val* Employees.adhour
        self.salary = self.salary + self.addtion_salary
    
    def set_Emp(self, nssn, nname, nsalary, ncourse):
        self.SSN = nssn
        self.Name = nname
        self.salary = nsalary
        self.course = ncourse
        conn = sqlite3.connect('information_univarsity.db')
        cur = conn.cursor()
        qinsert2 = f'insert into Employees(SSN, Name, salary, Major) values({self.SSN}, {self.Name}, {self.salary}, {self.course});'
        cur.execute(qinsert2)
        conn.commit()
        conn.close()


class Instructor(Employees):
    price_hour = 15
    def __init__(self,  SSN, Name, salary, course, hours):
        super().__init__( SSN, Name, 0, course, addtion_salary = 0)
        self.hours = hours
        
    
    def calculate_Salaries(self,new_hours):
        self.salary = new_hours * Instructor.price_hour

    def set_infoi(self, salary, hours, course):
        self.salary = salary
        self.course = course
        self.hours = hours
        self.course = course


s1 = Student(1, 'aseel', "CS", 20, 4, 91.4)
#s1.set_student(3, 'aseel', "CS", 20, 4, 91.4)
s2 = Student(2, 'ruba', "CE", 19, 3, 95)
e1 = Employees(1, 'ahmad', 2000, "cs")

