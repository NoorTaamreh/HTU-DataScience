#Session114
from weakref import ref
import firebase_admin
from firebase_admin import credentials 
from firebase_admin import db

# logging in using private key
cred = credentials.Certificate('C:\\Users\\USER\\Downloads\\كتب\\HTU\\Data Science\\Code\\Data base\\session14a-firebase-adminsdk-5rmhe-9d308974d6.json')
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://session14a-default-rtdb.firebaseio.com/' , 'httpTimeout' : 30})

print('logged in to firebase')

ref='newref1'
root=db.reference(ref)
x=60
root.set(x)

ref='newref1'
root=db.reference(ref)
x=700
root.set(x)
data=root.get()  #to print the data which is related to this root
print(data)

ref = "newref3/"
root = db.reference(ref)

# writing on the database
x = { "sub20": 70}
root.set(x)

#subvalue
ref = "newref/sub1/" 
root = db.reference(ref)
x = { "sub20": 70}
root.set(x)
data=root.get()
print(data)

#overwrite
ref='newref4'
root=db.reference(ref)
x='Test1'
root.set(x)
x='test2'
root.set(x)

data=root.get()  #to print all the data in the root
print(data)


