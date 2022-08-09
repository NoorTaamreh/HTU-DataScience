#you must be in the same directory as the database file to run this code - open folder in which you save this code then run this code
import sqlite3 
conn = sqlite3.connect('Students.db') #create a new database if the database doesn't already exist
cur=conn.cursor() #get a cursor object used to execute SQL commands

Drop='''DROP TABLE IF EXISTS StudentsInfo '''
cur.execute(Drop) #drop the table if it already exists


query1='''CREATE TABLE StudentsInfo
(
    StudentID int NOT NULL,
    StudentName NCHAR(10) NOT NULL,
    StudentPhone int NOT NULL,
    CourseID INT NOT NULL,
    CONSTRAINT FKSCourseID
     FOREIGN KEY (CourseID)
     REFERENCES Course(CourseID)
    PRIMARY KEY (StudentID)
    );'''
cur.execute(query1)
    

query2='''DROP TABLE IF EXISTS Course'''
cur.execute(query2)

query3='''CREATE TABLE Course
(
    CourseID int NOT NULL,
    CoursetName NCHAR (10) NOT NULL, 
    TutorName NCHAR (10) NOT NULL,
    University NCHAR (10) NOT NULL,
    PRIMARY KEY (CourseID)
);'''
cur.execute(query3)

#insert data into studentsinfo table
query4= '''INSERT INTO StudentsInfo values(1,'Noor',1111,1)'''
query5=''' INSERT INTO StudentsInfo values(2,'Sara',2222,1)'''
query6=''' INSERT INTO StudentsInfo values(3,'Salma',3333,3)'''
query7=''' INSERT INTO StudentsInfo values(4,'Sama',4444,4)'''
query8=''' INSERT INTO StudentsInfo values(5,'Nada',5555,2)'''
query9 ='''INSERT INTO StudentsInfo values(6,'Maryam',6666,5)'''
query10 ='''INSERT INTO StudentsInfo values(7,'Morya',7777,5) '''

#insert data into course table
query11=''' INSERT INTO Course values(1,'Python','Yazan','HTU')'''
query12=''' INSERT INTO Course values(2,'SQL','Mohanad','HTU')'''
query13 ='''INSERT INTO Course values(3,'DigitalMedia','Lina','JMI')'''
query14 ='''INSERT INTO Course values(4,'Podcast','Lina','JMI')'''
query15=''' INSERT INTO Course values(5,'History','Haya','BAU') '''

cur.execute(query4)
cur.execute(query5)
cur.execute(query6)
cur.execute(query7)
cur.execute(query8)
cur.execute(query9)
cur.execute(query10)
cur.execute(query11)
cur.execute(query12)
cur.execute(query13)
cur.execute(query14)
cur.execute(query15)

q=''' SELECT * FROM StudentsInfo '''
Data=cur.execute(q).fetchall() #fetch all the data from the table
print(Data) #print the data in the table
print(Data[:2]) #print first two rows of the table

#Left join between studentsinfo and course
q=''' SELECT A.StudentID,A.StudentName,A.StudentPhone,B.CoursetName,B.TutorName,B.University
FROM StudentsInfo A
LEFT JOIN Course B
ON A.CourseID=B.CourseID '''
Data=cur.execute(q).fetchall() #fetch all the data from the table
print(Data)

# Data2=Q1.fetchall()
# print(Data) 

conn.commit()
conn.close()
