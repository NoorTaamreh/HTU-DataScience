from firebase import firebase
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db

#method from youtube
#create a connection to the database 
conn=firebase.FirebaseApplication('https://tempretureproject-default-rtdb.firebaseio.com/', None)

while True:
    temp=int(input('Enter the temperature: '))
    data={'Temperature':temp}
    result =conn.post('/TempretureProject/', data)
    print(result)

while True:
    try:
        #get the data from the database
        data=conn.get('/TempretureProject/', None)
        print(data)
        break
    except:
        print('Error')
        break
  
#method 2  
# cred = credentials.Certificate('C:\\Users\\USER\\Downloads\\كتب\\HTU\\Data Science\\Code\\Data base\\session14a-firebase-adminsdk-5rmhe-9d308974d6.json')
# firebase_admin.initialize_app(cred, {'databaseURL' : 'https://session14a-default-rtdb.firebaseio.com/' , 'httpTimeout' : 30})
# Temperature = db.reference('TempretureProject/') 
# #create a connection to the database
# while True:
#     temp=int(input('Enter the temperature: '))
#     data={'Temperature':temp}
#     result =cred.post('/TempretureProject/', data)
#     print(result)
    
