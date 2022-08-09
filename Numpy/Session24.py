import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

data=[{'A':1,'B':2},{'A':10,'B':20,'C':3}]

#create dataframe from series
data={'one':pd.Series([1,2,3],index=['a','b','c']),
      'two':pd.Series([10,20,30,40],index=['a','b','c','d'])}
df=pd.DataFrame(data)
print(df)
print(df['one'])

#add a new column to the dataframe
df['three']=pd.Series([100,200,300],index=['a','b','c'])
print(df)

#add a new column by using the existing column
df['four']=df['one']+df['three']
print(df)
print(df.four) #print the new column

#delete a column
del df['four']
print(df)

#using pop method to delete a column
df.pop('three')
print(df)

#select row to the dataframe
print(df.loc['a'])

#select the row by index
print(df.iloc[1])

#select multiple rows to the dataframe usinf slicing
print(df.iloc[2:4])

#addind a new row to the dataframe using append
df2=pd.DataFrame([[5,6,7],[8,9,10]],columns=['A','B','C'],index=['e','f'])

df3=pd.DataFrame([[11,12,13],[14,15,16]],columns=['A','B','C'] )
#when we append data and dataframe, the dataframe will be concatenated and the index will be reset

df=df.append(df2)
df=df.append(df3)
print(df)

#drop a row from the dataframe
df=df.drop(0)
print(df)

#transpose the dataframe
print(df.T) 

#sort the dataframe
print("sort the dataframe\n",df.sort_index(axis=1,ascending=False))
print(df.sort_values(by='A'))


print('Shape of the data frame',df.shape) #print shape of the dataframe
print('size of the data frame',df.size) #print size of the dataframe
print(df.dtypes) #print the data type of the dataframe

print('the mean of each column\n',df.apply(np.mean)) #print the mean of each column
# x=df.apply(np.mean),axis=1
#print('the mean of each row\n',x) #print the mean of each row


#deleting multiple rows using slicing
df=df.drop(df.index[0:2])
print('drop multiple rows using slicing\n',df)

#df=df.df=df.drop(df.index[0:2], axis=0)

#deleting multiple columns using slicing
df=df.drop(df.columns[0:2],axis=1)
print('drop multiple columns using slicing\n',df)


df=df.drop(labels=["A","B"],axis=1)
print(df)

df = df.astype({"C": int},errors='raise')
print(df.dtypes)

