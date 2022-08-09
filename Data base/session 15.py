import requests

res=requests.get('https://httpbin.org/status/404')

# x=res.json()
# print(x)

y=res.text
print(y)

z=res.status_code
print(z)

#---------eg2--------
res=requests.get('https://pynative.com/python-json-load-and-loads-to-parse-json/')
print(res.text)
print(res.status_code)

res2=requests.api
print(res2.sessions)

requests.get('https://api.github.com/search/repositories',params={'q': 'requests+language:python'}, headers={'Accept': 'application/vnd.github.v3.text-match+json'},)
print(res.status_code)
print(res.json().keys())