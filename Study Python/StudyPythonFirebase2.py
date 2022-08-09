#create connection to firebase database
from weakref import ref
import firebase_admin
from firebase_admin import credentials 
from firebase_admin import db


cred = credentials.Certificate('C:\\Users\\USER\\Downloads\\كتب\\HTU\\Data Science\\Code\\Data base\\session14a-firebase-adminsdk-5rmhe-9d308974d6.json')
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://session14a-default-rtdb.firebaseio.com/' , 'httpTimeout' : 30})

# Get a database reference to our blog.
ref = db.reference('server/saving-data/fireblog')
users_ref = ref.child('users') #create a new child of the root = sub value

#method 1:set a value to the database (overwrite)
users_ref.set({
    'alanisawesome': {
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
    },
    'gracehop': {
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
    }
})

#method2
users_ref.child('alanisawesome').set({
    'date_of_birth': 'June 23, 1912',
    'full_name': 'Alan Turing'
})
users_ref.child('gracehop').set({
    'date_of_birth': 'December 9, 1906',
    'full_name': 'Grace Hopper'
})

#The above two examples - writing both values at the same time 
# as an object and writing them separately to child locations - 
# will result in the same data being saved to your database:

{
  "users": {
    "alanisawesome": {
      "date_of_birth": "June 23, 1912",
      "full_name": "Alan Turing"
    },
    "gracehop": {
      "date_of_birth": "December 9, 1906",
      "full_name": "Grace Hopper"
    }
  }
}

#update the value we'll have only one child
users_ref.update({
    'alanisawesome': {
        'nickname': 'Alan Test'
    },
    'gracehop': {
        'nickname': 'Amazing Grace'
    }
})

users_ref.child('alanisawesome').update({
    'nickname': 'Alan Test 2 '}) #overwrite the value

users_ref.child('alanisawesome').update({
    'nickname2': 'Alan Test 2 '})     #add a new value as a sub value

#delete the value of a child location
# users_ref.child('alanisawesome').delete({
#     'alanisawesome': {
#         'nickname': 'Alan The Machine'
#     }  })  

#add a new child location with overwriting the value
posts_ref = ref.child('posts')
new_post_ref = posts_ref.push()

new_post_ref.set({
    'author': 'gracehop',
    'title': 'Announcing COBOL, a New Programming Language'
})

posts_ref.push({
    'author': 'Raoom',
    'title': 'Sringth of the Heart'
})

post_id = new_post_ref.key #get the key of the new child

# We can also chain the two calls together
# posts_ref.push().set({
#     'author': 'Yazan',
#     'title': 'ML'
# }) 

new_post_ref.child('Test').set('Yazan')
#a push() function that generates a unique key for each new child.
