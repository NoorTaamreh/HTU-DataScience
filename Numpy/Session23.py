import numpy as np

array=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
# print(array)
# #transpose of array is same as transpose of matrix
# print(array.T)

list=[1,2,3,4,5,5,4,4,4,5,5,1,1,2]
#find no of occurence of each element in list
print(np.unique(list))#unique elements in list
x=np.unique(list,return_counts=True) #unique elements in list and no of occurence of each element
print(x)
# print(np.unique(list,return_counts=True))

values = np.array([1,2,3,1,2,4,5,6,3,2,15])
searchval = 2
ii = np.where(values == searchval)[0] #find the index of searchval in values
print(ii) #index of searchval in values
print(len(ii)) #no of occurence of searchval in values

#reverse for an array
print(np.flip(values))

#reverse for an array using slice
print(values[::-1]) #reverse the array

#vertical stack
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print(np.vstack((a,b)))

#horizontal stack
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print(np.hstack((a,b)))


#compute the min/max of each 
#np.random

import pandas as pd
# s=pd.Series()
# data=np.array['a','b','c','d','e',np.dtype('<U10')]
# s=pd.Series(data)
# print(s)

# data =['A': 0 , 'B': 1 , 'C': 2 , 'D': 3 , 'E': 4]
# print(data)

#creating aseries from scalar
s= pd.Series(5,index=['A','B','C','D','E'])
print(s)
print(s.index)
print(s.values)
print(s['C'])

#CREATING dataframe from series
data=[['Noor',4],['Raj',5],['Sai',6],['Ram',7]]
df=pd.DataFrame(data)
df=pd.DataFrame (data, columns = ['name', 'age'])
df=pd.DataFrame (data, index= ['R1','R2','R3','R4'])
print(df)
print(df['R1'][0]) 

       