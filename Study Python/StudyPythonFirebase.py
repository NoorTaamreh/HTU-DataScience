#create connection to firebase database
from logging import root
import firebase_admin  
from firebase_admin import credentials  
from firebase_admin import db

#logging in using private key
#use credentials to read the private key
cred = credentials.Certificate('C:\\Users\\USER\\Downloads\\كتب\\HTU\\Data Science\\Code\\Assignment\\assignment.json') 
#initialize the app with the private key and the database url
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://assignment-46b5c-default-rtdb.firebaseio.com/' , 'httpTimeout' : 30}) 

#Setting the location where the data will be stored
#create a reference to the database
ref='StudentsInfo'
root = db.reference(ref) #as a cursor

#write data to the database
q1={'StudensID':{1:'Noor',2:'Sara',3:'Salma',4:'Sama',5:'Nada',6:'Maryam',7:'Morya'},
    'Phone':{'Noor':1111,'Sara':2222,'Salma':3333,'Sama':4444,'Nada':5555,'Maryam':6666,'Morya':7777},
    'StudentCourseID':{'Noor':1,'Sara':1,'Salma':3,'Sama':4,'Nada':2,'Maryam':5,'Morya':5}
    }
root.set(q1)

# q1={'StudentID':1,'StudentName':'Noor','StudentPhone':1111,'CourseID':1}
# root.set(q1)
# q2={'StudentID':2,'StudentName':'Sara','StudentPhone':2222,'CourseID':1}
# root.set(q2)
# q3={'StudentID':3,'StudentName':'Salma','StudentPhone':3333,'CourseID':3}
# root.set(q3)

ref='CourseInfo'
root2 = db.reference(ref)
q2={'CourseIdName':
        {'A':'Python',
        'B':'SQL', 
        'C':'DigitalMedia', 
        'D':'Podcast', 
        'E':'History'},
    'TutorName':
        {'Python':'Yazan',
         'SQL':'Mohanad',
         'DigitalMedia':'Lina',
         'Podcast':'Lina',
         'History':'Haya'},
    'University':
        {'Python':'HTU',
         'SQL':'HTU',
         'DigitalMedia':'JMI',
         'Podcast':'JMI',
         'History':'BAU'}
    }
root2.set(q2)

#to print the data from the database
data=root.get() #get the data from the database
print('This is the data in Students info table',data)

data=root2.get() 
print('This is the data in Course table',data)

# #get the data from CourseID=1
# data=root2.child('CourseID').get()
# print('This is the data in Students info table for CourseID=1',data)


# q1={'CourseID':1,'CoursetName':'Python','TutorName':'Yazan','University':'HTU'}
# root2.set(q1)
# q2={'CourseID':2,'CoursetName':'SQL','TutorName':'Mohanad','University':'HTU'}
# root2.set(q2)

# q2=60
# root2.set(q2)

#set value to the data base without overwriting the previous data
# root.update({'StudentID':1,'StudentName':'Noor','StudentPhone':1111,'CourseID':1}) 
# root.update({'StudentID':2,'StudentName':'Sara','StudentPhone':2222,'CourseID':1}) 
# root.update({'StudentID':3,'StudentName':'Salma','StudentPhone':3333,'CourseID':3})
# root.update({'StudentID':4,'StudentName':'Sama','StudentPhone':4444,'CourseID':4})
# root.update({'StudentID':5,'StudentName':'Nada','StudentPhone':5555,'CourseID':2})
# root.update({'StudentID':6,'StudentName':'Maryam','StudentPhone':6666,'CourseID':5})
# root.update({'StudentID':7,'StudentName':'Morya','StudentPhone':7777,'CourseID':5})

#add subvalue to the data base
# ref='Test/Test2'
# root3 = db.reference(ref)
# q={'Test3':70}
# root3.set(q)


