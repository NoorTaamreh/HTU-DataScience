# list=[1,22,3,4,55,67,8,9]
# input x
# if x in list:
#binary search
# def function(list,num)  :
# list=[2,3,4,5,6,9,10,3]
#---------
# x=['a',1,'b',2,'c',3]
# print(x.pop())
#-------
from collections import deque
num=deque()
print(type(num))
num.append(99)
num.append(100)
num.append(200)
last_num=num.pop()
print(last_num)
first_num=num.popleft()
print(first_num)
print(num)
#----stack-----
class Stack:
    def __init__(self):
        self.stack = []
    
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)
    
    def size(self):
        return len(self.stack)

x = Stack()
#------
class Quee:
    def __int__(self):
        self.quee=[]
    
    def pop(self):
        return quee[0]
    
    def size(self):
        return len(self.Quee)   
k
x=Quee()

 
    
 