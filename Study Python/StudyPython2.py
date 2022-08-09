#Def-----------
print("Def Function eg.")

def Testfunction():
    print("First Function")

Testfunction()

def Sum(x,y):
    return x+y

Answer=Sum(7,8)

print(Answer)

#---------------------
def changelist(L):
    L.append(['A','B','C'])
    print("Values inside the function",L)
    return

L=[1,2,3]
changelist(L)
print("Values outside the function",L)

#----------------------
#Required Arquments
def Test(x):
    print(x)
    return

Test(5)
#Test() missing 1 required positional argument: 'x'
#----------------------
#Keyword Arquments
def Test2(x):
    print(x)
    return
Test2(x=20)

def my_function(child3, child2, child1):
      print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#----------------------
#Defult Arquments
def Test3(x=77):
    print(x)
    return

Test3(100)
Test3()

#----------------------
#VAR-Length Arquments
def VarFunction(x,*var):
    print(x)
    
    for y in var:
        print(y)
    return

VarFunction('Yes')
VarFunction(1,2,3)   
#---------------------
GlobalVar=7

def Sum(x,y):
    GlobalVar=x+y
    print("Inside",GlobalVar)
    return GlobalVar

Sum(10,30)
print("outside",GlobalVar) 

#---------------------
print('Regex eg.')

import re
from typing import Pattern
string ='Hello 12 HI 2 HODEY 2022'
pat='\D+'

Result=re.findall(pat,string)
print(Result)
#---------------------
import re
string ='Hello 12 HI 2 HODEY 2022'
pat='\D'

Result=re.findall(pat,string)
print(Result)
#---------------------
import re
string ='Hello 12 HI 2 HODEY 2022'
pat='\d+'

Result=re.findall(pat,string)
print(Result)
#---------------------
import re
string ='Hello 12 HI 2 HODEY 2022'
pat='\d'

Result=re.findall(pat,string)
print(Result)
#--------------------------
import re

S= 'python is fun'
Match=re.search('python',S)

if Match:
    print("Pattern found inside the string")
else:
    print("Pattern Not found ")
    
#--------------------------
import re
S="ABC 12\ DE 23 \n F45 6"
Pattren='\s+'
Replace='N'
NewString=re.sub(Pattren,Replace,S)
print(NewString)
#--------------------------
import re
S="ABC 12\ DE 23 \n F45 6"
Pattren='\S+'
Replace='N'
NewString=re.sub(Pattren,Replace,S)
print(NewString)
#--------------------------
import re
S="ABC 12& DE 23 \n F45 6"
Pattren='\S+'

NewString=re.findall(Pattren,S)
print(NewString)
#--------------------------
import re
S="ABC 12 DE 23 \n F45 6"  #will take the space next \n
Pattren='\s+'

NewString=re.findall(Pattren,S)
print(NewString)
#--------------------------