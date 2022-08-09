from webbrowser import get
from flask import Flask,render_template ,request
import json
import sqlite3
import requests

res=requests.get('http://google.com')
#print(res.json()) #convert the data to json
print(res.text) #convert the data to text
print(res.status_code) #get the status code

res=requests.get('https://api.github.com/search/repositories',
                 params={'Q':'requests+langauge=python'},
                 headers={'accept':'application/vnd.github.v3.text-match+json'},) #get the data from the website

# print('Github',res.status_code)
# print(res.text)
# print(res.json().keys()) #get the keys of the json
# print(res.json()['items'][0])#get the first item from the list
# print(len(res.json()['total_count'])) #get the length of the total_count
# print(res.json()['total_count']) #get the total count


#post request
post= requests.post('https://httpbin.org/post',data={'name':'test'}) #send data to the website as dictionary
print('response status1',post.status_code)
# post= requests.post('https://httpbin.org/post',data=[('name2':'test2')]) #send data to the website as list of tuples
# print('response status2',post.status_code)

#----------
app=Flask(__name__)

@app.route("/")  #decorator to define the route    #/ is the root route     
def hello1():
    return 'Hello World'

@app.route("/Test")  #decorator to define the route        
def hello():
    return 'Hello Test'

@app.route("/new")  #decorator to define the route
def index():
   return json.dumps({'Name':'Noor',
                      'Email':'Noor@test.com'}) #convert the data to json 
   
@app.route("/new2")  #decorator to define the route
def index2():
   return{'Name':'Noor','Email':'Noor@test.net'} #return the data as dictionary

#dosen't work here with post request ???
# @app.route("/new3", methods=['post'])  #specify the method to be used
# def index3():
#        return{'Name':'Noor','Email':'Noor@testpost.org'}
   
@app.route("/new4", methods=['get'])  #specify the method to be used   
def index4():
       return{'Name':'Noor','Email':'Noor@testget.org' }  
   
@app.route("/new5/<name>")  #specify variable in the route
def index5(name):
    print('Hello %s' %name) #WILL NOT print out  IN the browser just in the terminal
    return{'Name':name,'Email':name+'@testvar.org'}

# @app.route("/store", methods=['post'])  #specify the method to be used
# def store():
#     data=dict(flask.request.form)
#     print(data,type(data))
#     sent=data.pop('sent')
#     capturetime=data.pop('capturetime')
#     db_path='/home/noor/Desktop/test.db' #path to the database
#     db_path='databases/'+data.pop('gate')+".db"
#     db=sqlite3.connect(db_path)
#     db=Database(db_path)
#     db.connect()
#     cur=db.get_cursor()
#     Q1="INSERT INTO test (sent,capturetime) VALUES (77,44)"
#     db.send_query(Q1,(sent,capturetime))
#     db.send_query(cur,Q1)
#     db.close_connection()
#     #call the api to store the data in the database
#     return{SUCCESS:'Data stored'}
    

@app.route('/index') #to render the html page
def ind():
    return render_template('index.html')
    
@app.route('/index2') 
def new6():
    return str(request.args('n'))

@app.route('/test7')
def new7():
    x=int(request.args.get('x'))
    y=int(request.args.get('y'))
    return str(x*y)

if __name__=='__main__':
    app.run()
