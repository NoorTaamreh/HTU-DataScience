import requests

url = 'http://127.0.0.1:5000/get_image'
files = {'image': open('/mnt/c/Users/yazan/Desktop/test2.jpg', 'rb')}
x = requests.post(url, files=files)
print(x.text)
