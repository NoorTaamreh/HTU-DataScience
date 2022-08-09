from unicodedata import name
import numpy as np
#import matplotlib.pyplot as plt

a=np.array([1,2,3,4,5,6,7,8,9,10]) #one dimensional array
print(a)

b=np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]) #two dimensional array
print(b)

c=np.array([1,2,3,4,5,6,7,8,9,10],ndmin=2) #spisefy the dimension of array
print(c)
#c[0] ok c[1] out of range
d=np.array([1,2,3,4,5,6,7,8,9,10],dtype=np.float64) #one dimensional array with float64

DT=np.dtype([('name','S10'),('age',int),('marks',float)]) #create a dtype

DT=np.dtype(np.float64) 
print(DT)

DT=np.dtype(['age',np.int])

DT=np.dtype([('name','S10'),('age','i4'),('marks','f4')]) #create a dtype
students=np.array([('raj',20,50),('sai',21,60),('ram',22,70)],dtype=DT) #create array with dtype
print(students['name']) #print the name of students
print(students['age'][1]) #sai
print(students[0]) #print the first row

