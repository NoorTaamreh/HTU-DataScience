import requests

app=requests.get('http://127.0.0.1:5000/test7',{'x':10,'y':7})
print(app.text) #to print the result in the text format (string)
print(app.url) #to print the url


