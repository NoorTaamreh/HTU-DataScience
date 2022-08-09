import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data={'one':pd.Series([1,2,3,4,5,6],index=['a','b','c','e','f','g']),
      'two':pd.Series([10,20,30],index=['a','b','c'])}
df=pd.DataFrame(data)
print(df)

#fill the missing values with 0
df.fillna(22)

#drop na values
df=df.dropna()
print (df)

# df2=pd.DataFrame([[5,6,7],[8,9,10]],columns=['A','B','C'],index=['e','f'])
# df3=pd.DataFrame([[11,12,13],[14,15,16]],columns=['A','B','C'] )

# df=df.append(df2)
# df=df.append(df3)
# print(df)

#query the dataframe column one 
print('Q1\n',df[df['one']<2])

print('Q2\n',df.query('one>2')) #using query method

#query for multiple columns
print('Q3\n',df[(df['one']>2) & (df['two']>10)])


#replace the value in the dataframe
# df.replace(NaN,100,inplace=True)
# print(df)

# #Ruba's code
# data = {
#   "name": ["Sally", "Mary", "Sally"],
#   "age": [50, 40, 30],
#   "qualified": [True, False, False],
#   "ID":[10,20,30]
# }

# df=pd.DataFrame(data)
# print(df)

# df['name'] = df['name'].replace(['Sally'],'Tala')
# print(df)

# #Aseel's code
# # Below are quick example
# # convert "Fee" from string to float

# data = ({
#          'Fee' :['22000','25000' ,'23000','24000','26000'],
#          'Discount':['1000',np.nan,'1000',np.nan,'2500']})

# df = pd.DataFrame(data)

# print(df.dtypes)

# df['Fee'] = df['Fee'].astype(float)
# print(df.dtypes)

# # Convert multiple columns
# df = df.astype({'Fee':'float','Discount':'float'})


#Abdulla's code
d = {"country":pd.Series(["Brazil","Russia","India","China","South Africa"]),

    "capital":pd.Series(["Brasilia","Moscow","New Delhi","Beijing","Pretoria"]),

    "area":pd.Series([8.516, 17.10, 3.286, 9.597, 1.221]),

    "population":pd.Series([200.4, 143.5, 1252, 1357, 52.98])}

df = pd.DataFrame(d)

df2 = df.query('country == "Russia"')
print(df2)

#matloblib in machine learning
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
y=np.array([[10,20,30],[40,50,60],[70,80,90]])
# plt.plot(x,y) #plotting the graph
# plt.show() #showing the graph

# plt.plot(x,y,'o') #plotting the graph with dots
# plt.show()

# plt.plot(x,y,marker='*')#plotting the graph with dots
# plt.show()

# plt.plot(x,y,marker='o',color='red')#plotting the graph with dots and color
# plt.show()

# plt.plot(x,y,':r') #plotting the graph with dots using : and color r =  ' : r '
# plt.show()

# plt.plot(x,y,'o-.g',ms=7) #setting the marker size and color
# plt.show()

#graph with grid
# plt.plot(x,y,'o-')
# plt.xlabel('x-axis') #setting the x-axis label
# plt.grid(True)
# plt.show()

plt.subplot(1,2,1)#setting the subplot
plt.show

