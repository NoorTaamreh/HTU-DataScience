import json
#some json data as a string
x= '{ "name":"John", "age":30, "city":"New York"}' 
y=json.loads(x) #loads the json data into a python dictionary (converts json to python dictionary)
print(y)
print(x[0])
print(x[3])

#python dictionary to json
dic= {'name': 'John', 'age': 30, 'city': 'New York'}
z=json.dumps(dic) #dumps the python dictionary into a json string (converts python dictionary to json)
print(z)
print(dic['name'])
print(z[0])
print(z[3])


