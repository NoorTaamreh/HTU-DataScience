#create connection to firebase database
from webbrowser import get
from flask import Flask,render_template ,request
import json
import sqlite3
import requests
from logging import root
import firebase_admin  
from firebase_admin import credentials  
from firebase_admin import db

#logging in using private key
cred = credentials.Certificate('C:\\Users\\USER\\Downloads\\كتب\\HTU\\Data Science\\Code\\Data base\\session14a-firebase-adminsdk-5rmhe-9d308974d6.json')
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://session14a-default-rtdb.firebaseio.com/' , 'httpTimeout' : 30})

#Setting the location where the data will be stored
#create a reference to the database
Student = db.reference('StudentsInfo') #as a cursor

#write data to the database
q1={'StudensID':
        {1:'Noor',
        2:'Sara',
        3:'Salma',
        4:'Sama',
        5:'Nada',
        6:'Maryam',
        7:'Morya'},
    'Phone':
        {'Noor':1111,
         'Sara':2222,
         'Salma':3333,
         'Sama':4444,
         'Nada':5555,
         'Maryam':6666,
         'Morya':7777},
    'StudentCourseID':
        {'Noor':1,
         'Sara':1,
         'Salma':3,
         'Sama':4,
         'Nada':2,
         'Maryam':5,
         'Morya':5}
    }
Student.set(q1) #set the data to the database StudentInfo node
new_StusentInfo=Student.child('Country')
new_StusentInfo.set({'Noor':'Jordan',
                     'Sara':'Jordan',
                     'Salma':'Syria',
                     'Sama':'Syria',
                     'Nada':'Iraq',
                     'Maryam':'Sudia Arabia',
                     'Morya':'Sudia Arabia'})

#update the data in the database overwrite the old data
new_StusentInfo.update({'Morya':'Palestine'}) #just modify the data in Morya

#update the data if the data not exixt add it
new_StusentInfo.update({'Sora':'Palestine'})


#add new data to the database 
Course = db.reference('CourseInfo')
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
Course.set(q2) #set the data to the database course node


#add sub-child to the course without overwriting the previous data and without unique key
new_CourseInfo=Course.child('TutorEmail')
new_CourseInfo.set({
        'Yazan':'yazan@htu.edu.jo',
         'Mohanad':'mohanad@htu.edu.jo',
         'Lina':'lina@jmi.edu.jo',
         'Haya':'haya@bau.edu.jo'
})


#delete data from the database
new_CourseInfo.child('Mohanad').delete() #delete the data of the child Yazan 

#print the data from the database
print(Course.get())

post= requests.post('https://session14a-default-rtdb.firebaseio.com/',data={'name':'test'})
print(post.status_code)



# import requests

# app=requests.get('http://127.0.0.1:5000/test7',{'x':10,'y':7})
# print(app.text) #to print the result in the text format (string)
# print(app.url) #to print the url
