import time
# def fact(x):
#     result=x*(x-1)
#     x-=1
#     if x==1:
#         return result
#     else:
#         fact(x)
        
# print(fact(3))

#-----------------
import time

start = time.time()
def factorial(num):
    if num<=1:
        return num
    else:
        return num*factorial(num-1)
    
print(factorial(3))
print(time.time() - start)

#-----------------
start = time.time()
def fact(num):
    y=1
    for i in range(num):
        y=(i+1)*y
    return y
print(time.time() - start)
#-------------
def function(num):
    list=[]
    for i in num:
        list.append
    