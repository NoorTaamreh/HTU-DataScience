import sqlite3

conn = sqlite3.connect('Task2Session12.db') 

cur =conn.cursor()

Drop1='''DROP TABLE IF EXISTS Course'''
cur.execute(Drop1)

query1='''CREATE TABLE Course
(
    CourseID int NOT NULL,
    CoursetName NCHAR (10) NOT NULL, 
    TutorName NCHAR (10) NOT NULL,
    University NCHAR (10) NOT NULL,
    PRIMARY KEY (CourseID)
);'''


# Drop2='''DROP TABLE IF EXISTS Students'''
# cur.execute(Drop2)
# query2='''CREATE TABLE Students
# (
#     StudentID int NOT NULL,
#     StudentName NCHAR(10) NOT NULL,
#     StudentPhone int NOT NULL,
#     CourseID INT NOT NULL FOREIGN KEY REFERENCES Course(CourseID)
#     PRIMARY KEY (StudentID) 
# );'''

Drop2='''DROP TABLE IF EXISTS Students'''
cur.execute(Drop2)

# query2='''CREATE TABLE Students
# (
#     StudentID int NOT NULL,
#     StudentName NCHAR(10) NOT NULL,
#     StudentPhone int NOT NULL,
#     CourseID INT NOT NULL,
#     CONSTRAINT FKSCourseID
#      FOREIGN KEY CourseID
#      REFERENCES Course(CourseID) 
#     PRIMARY KEY (StudentID)


# );'''

Q='''CREATE TABLE Students
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
cur.execute(Q)
# query3=''' ALTER TABLE Students
# ADD FOREIGN KEY (CourseID) REFERENCES Course(CourseID);'''

# query3=''' CONSTRAINT fk_CourseID
#     FOREIGN KEY CourseID
#     REFERENCES Course(CourseID)
#     CONSTRAINT FKCourseID FOREIGN KEY CourseID REFERENCES Course(CourseID)  
# '''

query4= '''INSERT INTO Students values(1,'Noor',1111,1)'''
query5=''' INSERT INTO Students values(2,'Sara',2222,1)'''
query6=''' INSERT INTO Students values(3,'Salma',3333,3)'''
query7=''' INSERT INTO Students values(4,'Sama',4444,4)'''
query8=''' INSERT INTO Students values(5,'Nada',5555,2)'''
query9 ='''INSERT INTO Students values(6,'Maryam',6666,5)'''
query10 ='''INSERT INTO Students values(7,'Morya',7777,5) '''


query11=''' INSERT INTO Course values(1,'Python','Yazan','HTU')'''
query12=''' INSERT INTO Course values(2,'SQL','Mohanad','HTU')'''
query13 ='''INSERT INTO Course values(3,'DigitalMedia','Lina','JMI')'''
query14 ='''INSERT INTO Course values(4,'Podcast','Lina','JMI')'''
query15=''' INSERT INTO Course values(5,'History','Haya','BAU') '''

cur.execute(query1)
#cur.execute(query2)
#cur.execute(query3)
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

q='''SELECT *FROM Students'''
Data=cur.execute(q).fetchall()
print=(Data)
       
# query6 ='''SELECT * from Students'''
# cur.execute(query6)

conn.commit()
conn.close()

# SELECT CourseDS.CourseID
# FROM CourseDS
# INNER JOIN StudentsDS
# ON StudentsDS.CourseID = CourseDS.CourseID;
# ---------
# SELECT CourseDS.CourseID, StudentsDS.StudentName
# FROM StudentsDS
# LEFT JOIN CourseDS 
# ON StudentsDS.CourseID = CourseDS.CourseID
# ORDER BY StudentsDS.CourseID;
# --------
# SELECT CourseDS.CourseID, StudentsDS.StudentName
# FROM StudentsDS
# RIGHT JOIN CourseDS 
# ON StudentsDS.CourseID = CourseDS.CourseID
# ORDER BY StudentsDS.CourseID;
# --------