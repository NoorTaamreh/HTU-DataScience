CREATE TABLE Students
(
    StudentID int NOT NULL,
    StudentName NCHAR(10) NOT NULL, 
    PRIMARY KEY (StudentID)
);

CREATE TABLE Grade
(
  GradeID int NOT NULL,
  Grade NCHAR(10) NOT NULL, 
  PRIMARY KEY (GradeID)  
);

CREATE TABLE Faculty
(
    FacultyID int NOT NULL,
    FacultytName NCHAR(10) NOT NULL, 
    Phone INT NOT NULL, 
    PRIMARY KEY (FacultyID)
);

CREATE TABLE Course
(
    CourseID int NOT NULL,
    CoursetName NCHAR (10) NOT NULL, 
    FacultyID int NOT NULL,
    PRIMARY KEY (FacultyID)
);
ALTER TABLE Course
ADD FOREIGN key(FacultyID) REFERENCES Faculty(FacultyID)


CREATE TABLE StudentsGrade
(
    ID int NOT NULL,
    CourseID int NOT NULL,
    GradeID INT NOT NULL,
    StudentID INT FOREIGN KEY REFERENCES Students(StudentID)
    PRIMARY KEY (ID)
);

ALTER TABLE Course
ADD FOREIGN key(FacultyID) REFERENCES Faculty(FacultyID)

ALTER TABLE Grade
ADD FOREIGN key(GradeID) REFERENCES Grade(GradeID)


Insert INTO Students values(1,'Adams')
Insert INTO Students values(2,'Jones')
Insert INTO Students values(3,'Smith')
Insert INTO Students values(4,'Baker')

Select * From Students

Insert INTO Grade values(1,'A')
Insert INTO Grade values(2,'B')

Select * From Grade

Insert INTO Faculty values(1,'Howser',60192)
Insert INTO Faculty values(2,'Langley',45869)
Select * From Faculty

INSERT INTO Course values(1,'Data Base',1)
INSERT INTO Course values(2,'Program',2)
Select * From Course

UPDATE Faculty
 SET FacultytName='Howser2'

Delete from Course
 where CoursetName='Data Base'