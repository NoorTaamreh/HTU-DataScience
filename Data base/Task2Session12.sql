CREATE TABLE Students
(
    StudentID int NOT NULL,
    StudentName NCHAR(10) NOT NULL,
    StudentPhone int NOT NULL,
    CourseID INT NOT NULL FOREIGN KEY REFERENCES Course(CourseID)
    PRIMARY KEY (StudentID)   
);

CREATE TABLE Course
(
    CourseID int NOT NULL,
    CoursetName NCHAR (10) NOT NULL, 
    TutorName NCHAR (10) NOT NULL,
    University NCHAR (10) NOT NULL,
    PRIMARY KEY (CourseID)
);

Insert INTO Students values(1,'Noor',1111,)
Insert INTO Students values(2,'Sara',2222,)
Insert INTO Students values(3,'Salma',3333,)
Insert INTO Students values(4,'Sama',4444,)
Insert INTO Students values(5,'Nada',5555,)
Insert INTO Students values(6,'Maryam',6666,)
Insert INTO Students values(7,'Morya',7777,)

Insert INTO Course values(1,'Python','Yazan','HTU')
Insert INTO Course values(2,'SQL','Mohanad','HTU')
Insert INTO Course values(3,'DigitalMedia','Lina','JMI')
Insert INTO Course values(4,'Podcast','Lina','JMI')
Insert INTO Course values(5,'History','Haya','BAU')

