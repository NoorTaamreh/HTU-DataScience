# from crypt import methods
from tkinter import Y
from urllib import response
from flask import Flask, render_template, request
import json

from requests import post

app=Flask(__name__)

@app.route("/")
def hello():
    return 'Hello'

@app.route("/new")
def hello2():
    return 'Hello new'

@app.route("/test")
def test():
    return json.dumps({'Name':'Test','Email':'test@gmail.com'})



@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' %name

@app.route('/test3')
def index():
    return render_template('index.html')

@app.route('/test4')
def func1():
    return str(request.args.get('no'))

# @app.route('/test5/<num1>/<num2>')
# def func1(num1,num2):                  #don't use this way
#     return num1*num2

# @app.route('/test5')
# def func2():
#     str(request.args.get('num1','num2'))
#     return num1*num2

# @app.route('/test6')
# def func6():
#     x=request.args.get('x',type=int)
#     y=request.args.get('y',type=int)
#     return x*y

@app.route('/test7')
def func7():
    x=int(request.args.get('x'))
    y=int(request.args.get('y'))
    return str(x*y)

# @app.route("/test2",methods=['post'])
# def test():
#     return json.dumps({'Name':'Test','Email':'test@gmail.com'})

if __name__=='__main__':
    app.run()
    # app.run(debug=True)#to restart 
