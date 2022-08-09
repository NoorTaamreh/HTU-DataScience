class Student:
    def __init__(self, name, grade, gpa):
        self.name = name
        self.grade = grade
        self.gpa = gpa
    def get_info(self):
        print(self.name, self.grade, self.gpa)

ahmad = Student('ahmad', 88.34, 'B')
ahmad.get_info()


#2
class Students:
      def __init__(self, name, age,gender,grade):
    self.name = name
    self.age = age
    self.gender = gender
    self.grade = grade
 
  st1("Ahmad","11","mail","5")
  
#3
class Student:   
 def __init__(self, name, age, grade):
    self.name = name
    self.age = age  
    self.grade=grade         
 
s1=Student('Ahmad','26','3.0') 
print('name: ' + s1.name)
print('age: ' + s1.age)
print('grade: ' + s1.grade)


#4
class Students:
      def __init__(self, name, age,gender,grade):
    self.name = name
    self.age = age
    self.gender = gender
    self.grade = grade
 
  st1("Ahmad","11","mail","5")

#5
class Students:
    def __init__(self, name, age,gender,grade):
      self.name = name
      self.age = age
      self.gender = gender
      self.grade = grade

    def get_info(self):
        print(self.name,self.age,self.gender,self.grade)
 
st1=Students("Ahmad","11","male","5")
st1.get_info()


# 6 students 2 special
# payment 3000 then 4000 
# special students 10


#
class student:
    def_milestone = 3000
    def __init__(self, name, grade, GPA):
          self.name = name
          self.grade= grade
          self.GPA = GPA
    def get(self):
        print(self.name, self.grade, self.GPA)

S1 = student('a', 5, 90)
S2 = student('b', 6, 97)
S3 = student('c',6,80)
S4 = student('d',7, 50)
S5 = student('e', 8, 23)
S6 = student('f', 8, 50)
S2.def_milestone=100
S3.def_milestone =100
student.def_milestone = 4000

print(S2.def_milestone, student.def_milestone, S6.def_milestone)

#
class Student:
    fees=2000
    def __init__(self,name,grade,GPA):
        self.name=name
        self.grade=grade
        self.GPA=GPA
    def getName(self):
        return self.name, self.grade , self.GPA

st1=Student('lana','4','A')
st2=Student('zaid','5','B')
st3=Student('heba','5','c')
st4=Student('yara','3','A+')
st5=Student('salma','4','A+')
st6=Student('huda','7','B')
name1=st1.fees
name2=st2.fees
name3=st3.fees
st4.fees=100
st5.fees=100
name4=st4.fees
name5=st5.fees
name6=st6.fees
print('student1 fees is : ',name1)
print('student2 fees is : ',name2)
print('student3 fees is : ',name3)
print('student4 fees is : ',name4)
print('student5 fees is : ',name5)
print('student6 fees is : ',name6)

#
class school:
    
    # dunder function 
    def __init__(self, name, grade, GPA, email, special = 'No'):
        # these are called attributes to a class
        
        self.name = name
        self.grade = grade
        self.GPA = GPA
        self.email = email
        self.special = special
    
    def get_info(self):
        print('{} in the grade: {} got GPA: {} for more info: {} '.format(self.name,self.grade,self.GPA,self.email))
    
    special_price = 4000
    if self.special == 'yes' or self.special == 'Yes':
        special_price = 100

student_1 = school('ahmad ali', '10A', 3.5, 'ahmad@gmail.com', 'Yes')
student_2 = school('deema', '9A', 2.5, 'deema@gmail.com', 'No')

student_1.special_price()
student_2.special_price()

#
class Student:
    payment = 3000
    def __init__(self, firstname = 'empty', lastname = 'empty', grade = 00, gpa = 'undefined'):
        self.firstname = firstname
        self.lastname = lastname
        self.grade = grade
        self.gpa = gpa
    def get_gpa(self):
        grade = self.grade
        if grade > 90 and grade <= 100:
            self.gpa = "A+"
        elif grade > 80 and grade <= 90:
            self.gpa = "A-"
        elif grade > 70 and grade <= 80:
            self.gpa = "B+"
        elif grade > 60 and grade <= 70:
            self.gpa = "B-"
        elif grade > 49 and grade <= 60:
            self.gpa = "C"
        elif grade < 50:
            self.gpa = "F"
    def is_special(self):
        if self.gpa in ['A+', 'A-']:
            print('special student')
            self.payment = 100
        else:
            print('regular student')
    def get_info(self):
        self.get_gpa()
        print(self.firstname, self.lastname, self.grade, self.gpa, self.payment)

student1 = Student('ahmad', 'mahmoud', 88.43)
student2 = Student('John', 'Watson', 95.3)
student3 = Student('rami', 'tamer', 70.5)
student4 = Student('ahmad', 'mahmoud', 88.43)
student5 = Student('John', 'Watson', 95.3)
student6 = Student('rami', 'tamer', 70.5)

student1.get_info()
student1.payment = 4000
student1.is_special()
student1.get_info()

student2.get_info()
student2.payment = 4000
student2.is_special()
student2.get_info()

student3.get_info()
student3.payment = 4000
student3.is_special()
student3.get_info()

student4.get_info()
student4.payment = 4000
student4.is_special()
student4.get_info()

student5.get_info()
student5.payment = 4000
student5.is_special()
student5.get_info()

student6.get_info()
student6.payment = 4000
student6.is_special()
student6.get_info()