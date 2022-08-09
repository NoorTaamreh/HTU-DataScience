import sqlite3 
import os
import csv
from sqlite3 import Error


class Employee:
    def __init__(self, id, name, age, hire_date, hours_worked):
        self.id = id
        self.name = name
        self.age = age
        self.hire_date = hire_date
        self.hours_worked = hours_worked
        self.info()
     
    def info(self):
        print('inside database func')
        print(self.name)
        conn=sqlite3.connect('Information.db')
        cur=conn.cursor()
        
        query1=f'''INSERT INTO EmployeeInfo (EmployeeID,EmployeeName,EmployeeAge,EmployeeHire_date,EmployeeHours_worked) values ({self.id},"{self.name}",{self.age},{self.hire_date},{self.hours_worked})'''
        query2=f'''INSERT INTO EmployeeInfo (EmployeeID,EmployeeName,EmployeeAge,EmployeeHire_date,EmployeeHours_worked) values ({self.id},"{self.name}",{self.age},{self.hire_date},{self.hours_worked})'''
        query3=f'''INSERT INTO EmployeeInfo (EmployeeID,EmployeeName,EmployeeAge,EmployeeHire_date,EmployeeHours_worked) values ({self.id},"{self.name}",{self.age},{self.hire_date},{self.hours_worked})'''
        query4=f'''INSERT INTO EmployeeInfo (EmployeeID,EmployeeName,EmployeeAge,EmployeeHire_date,EmployeeHours_worked) values ({self.id},"{self.name}",{self.age},{self.hire_date},{self.hours_worked})'''
        print(query1)
        cur.execute(query1)
        cur.execute(query2)
        cur.execute(query3)
        cur.execute(query4)
        
        conn.commit()
        conn.close()  
        
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

class FullTime(Employee):
    def __init__(self, name, age, hire_date, hours_worked,salary):
        super().__init__(name, age, hire_date, hours_worked)
        self.salary = hours_worked * 20   

class PartTime(Employee):
    def __init__(self, name, age, hire_date, hours_worked,salary):
        super().__init__(name, age, hire_date, hours_worked)
        self.salary = hours_worked * 15
        
    
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
        
    def student_name(self):
        print('The name of the student is '+self.name.capitalize())
    
    def student_marks(self):
        if self.marks>=90:
            print('The student graguate with an A')
        elif self.marks>=80:
            print('The student graguate with a B')
        elif self.marks>=70:
            print('The student graguate with a C')
        elif self.marks>=60:
            print('The student graguate with a D')
        else:
            print('The student failed')
        
    
class major:
     def __init__(self,faculty,gba):
        self.faculty=faculty
        self.gbi=gba
    
class Subject(major):
     def __init__(self,name,code,credit,faculty,gba):
        self.name=name
        self.code=code
        self.super().__init__(faculty,gba)
        

Std1=Student('ahmed',20,90)
Std2=Student('mohamed',21,80)
Std3=Student('Amjad',22,70)

Employee1=Employee(1,'Sari',20,'12/1/12',20)
Employee2=Employee(2,'yazan',21,'12/2/12',15)
Employee3=Employee(3,'Amjad',22,'12/3/12',13)
Employee4=Employee(4,'Saed',23,'12/4/12',10)



#-------Q2 create database ------- 
import sqlite3
conn=sqlite3.connect('Information.db')
cur=conn.cursor()

Drop='''DROP TABLE IF EXISTS StudentsInfo '''
cur.execute(Drop)

Q1='''CREATE TABLE StudentsInfo
(StudentID int NOT NULL,
StudentName NCHAR(10) NOT NULL,
StudentAge int NOT NULL,
StudentMarks int NOT NULL)'''
cur.execute(Q1)

Drop2='''DROP TABLE IF EXISTS EmployeeInfo '''
cur.execute(Drop2)

Q2='''CREATE TABLE EmployeeInfo
(EmployeeID int NOT NULL,
EmployeeName NCHAR(10) NOT NULL,
EmployeeAge int NOT NULL,
EmployeeHire_date DATE NOT NULL,
EmployeeHours_worked int NOT NULL)'''
cur.execute(Q2)

conn.commit()
conn.close()
    
#------Q3--------
#export data in table EmployeesInfo as csv file
# sqlite3 -header -csv database.db "select * from EmployeeInfo;" > database.csv

# To view table data in table format
print ("******Employee Table Data*******")
conn=sqlite3.connect('Information.db')
cur = conn.cursor()
cur.execute('''SELECT * FROM EmployeeInfo''')
rows = cur.fetchall()
for row in rows:
    print(row)
    
# Export data into CSV file
print ("Exporting data into CSV............")
cursor = conn.cursor()
cursor.execute("select * from EmployeeInfo")
with open("employee_data.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t")
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)

# import time 
# dirpath = os.getcwd() + "/employee_data.csv"
# print(dirpath)
# time.sleep(20)
# print ("Data exported Successfully into {}").format(dirpath)


#----------Q4--------
nodes = ('A', 'B', 'C', 'D', 'E')
distances = {
    'A': {'B': 5, 'C': 2},
    'B': {'C': 2, 'D': 3},
    'C': {'B': 3, 'D': 7},
    'D': {'E': 7},
    'E': {'D': 9}}
current = 'A'
