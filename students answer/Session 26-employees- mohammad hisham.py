from datetime import datetime
import sqlite3
import pandas as pd
from attr import s

class DataBase:
    def __init__(self, dbname):
        self.conn = sqlite3.connect(f"{dbname}.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA journal_mode=WAL")
        self.conn.commit()
        
    def create_table(self, tbname, columns):
        self.cursor.execute(f"CREATE TABLE {tbname}({columns})")
        self.conn.commit()
    def insert_data(self, tbname, columns, values):
        self.cursor.execute(f"INSERT INTO {tbname}({columns}) VALUES ({values})")
        self.conn.commit()
    def call_data(self, tbname):
        self.cursor.execute(f"SELECT * FROM {tbname}")
        return self.cursor.fetchall()


class Employees:
    def __init__(self, emp_name, emp_position, starting_date, dbname):
        self.__emp_name = emp_name
        self.__emp_position = emp_position
        self.__starting_date= starting_date
        self.db = DataBase(f'{dbname}.db')
        self.db.cursor.execute("CREATE TABLE IF NOT EXISTS employee(emp_id INTEGER PRIMARY KEY AUTOINCREMENT, emp_name VARCHAR(100), emp_position VARCHAR(100), emp_starting_date VARCHAR(100))")
        self.db.insert_data("employee", "emp_name, emp_position, emp_starting_date", f"'{emp_name}', '{emp_position}', '{starting_date}'")

    def get_emp_name(self):
        return self.__emp_name
    def set_emp_name(self, name):
        self.__emp_name = name
    def get_starting_date(self):
        return self.__starting_date
    def set_starting_date(self, starting_date):
        self.__starting_date = starting_date
    def get_emp_position(self):
        return self.__emp_position
    def set_emp_position(self, position):
        self.__emp_position = position
    def calculate_salary(self):
        # calculate the salary of an employee : 
        pass

class Majors:
    def __init__(self, major_name, institute, degree):
        self.major_name = major_name
        self.institute = institute
        self.degree = degree

    def __repr__(self):
        return self.major_name, self.institute, self.degree

class Instructors(Employees):
    def __init__(self, emp_name, emp_position, starting_date, major_name, institute, years):
        super().__init__(emp_name, emp_position, starting_date, major_name, institute, years)
        self.major = Majors(major_name, institute, years)

class PartTime(Instructors):
    def __init__(self, emp_name, emp_position, starting_date, major_name, institute, years, salary_per_hour):
        super().__init__(emp_name, emp_position, starting_date, major_name, institute, years)
        self.salary_per_hour = salary_per_hour

# is = > inheritance or has composition       
# class Student(Majors):
#     def __init__(self, major_name, institute, degree, st_name, st_birthdate, st_class):
#         super().__init__(major_name, institute, degree)
#         self.st_name = st_name
#         self.st_birthdate = st_birthdate
#         self.st_class = st_class

class Student:
    def __init__(self, st_name, st_birthdate, st_class, major_name, institute, degree, dbname):
        self.st_name = st_name
        self.st_birthdate = st_birthdate
        self.st_class = st_class
        self.major = Majors(major_name, institute, degree)
        self.db = DataBase(f'{dbname}.db')
        self.db.cursor.execute("CREATE TABLE IF NOT EXISTS students(student_id INTEGER PRIMARY KEY AUTOINCREMENT, student_name VARCHAR(100), student_birthday VARCHAR(100), student_class VARCHAR(100), major_name VARCHAR(100), institute VARCHAR(100), degree VARCHAR(100))")
        self.db.insert_data("students", "student_name, student_birthday, student_class, major_name, institute, degree", f"'{st_name}', '{st_birthdate}', '{st_class}', '{major_name}', '{institute}', '{degree}'")

class Subjects(Majors):
    def __init__(self, major_name, institute, years, subject_name, author, references):
        super().__init__(major_name, institute, years)
        self.subject_name = subject_name
        self.author = author
        self.references = references


# is => inheritance or has => composition      


# mahmoud = Employees("Mahmoud Jamal", "Co-Manager", "12-12-2014", "practice")
# ahmad = Employees("ahmad mahmoud", "Lawyer", "17-12-2012", "practice")
# tamer = Employees("ahmad tamer", "HR", "12-11-2010", "practice")
# khalid = Employees("khalid mahmoud", "Manager", "17-12-2009", "practice")
# riad = Employees("riad mahmoud", "Customer Service", "07-01-2010", "practice")

# st_name, st_birthdate, st_class, major_name, institute, degree, dbname
# st1 = Student("Murad Rayan", "15-10-1999", "A15", "CyperSecurity", "Al hussien Technical Univerity", "Bachlor", "practice")
# st2 = Student("Ayman Mahmoud", "10-10-1999", "B12", "Full-Stack Development", "Al hussien Technical Univerity", "Bachlor", "practice")
# st3 = Student("Rashed Hussien", "18-08-1998", "S14", "E-Commerce", "Al hussien Technical Univerity", "Bachlor", "practice")
# st4 = Student("Hashim Abdullah", "30-01-2000", "A12", "Data Science", "Al hussien Technical Univerity", "Bachlor", "practice")
# st5 = Student("Emad Saif", "03-03-2001", "A10", "Cryptography Science", "Al hussien Technical Univerity", "Bachlor", "practice")

conn = DataBase("practice.db")
df_employee = pd.DataFrame(conn.call_data('employee'))
print(df_employee)
df_employee.to_csv("employee.csv")