import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#plot1
# x=np.array([[1,2,3],[4,5,6],[7,8,9,10]])
y=np.array([1,4,9,16,25,36,49,64,81,100])
z=np.array([5,10,15,20,25,30,35,40,45,50])
sizes=np.array([10,20,30,40,50,60,70,80,90,100])

plt.subplot(1,2,1)
plt.plot(z,y)
plt.title('z vs y')
#add supertitle
plt.suptitle('z vs y Graph')

plt.subplot(1,2,2)
plt.plot(y,z)
plt.title('y vs z')
# plt.scatter(y,z)
# plt.scatter(y,z,s=sizes,alpha=0.5)
# plt.scatter(y,z, alpha=np.array([0.3,0.5,0.7]), s= sizes)
# plt.colorbar()
# plt.bar(y,z,width=3)
# plt.barh(y,z,height=3)
# plt.show()

# plt.bar(y,z)
# plt.barh(y,z)
# plt.hist(y,z)
# plt.show()

y=np.array([23,35,70,150])
mylabel=np.array(['Python','C++','Java','Ruby'])
myexplode=np.array([0.1,0.1,0.1,0.1])
plt.pie(y,labels=mylabel,explode=myexplode)
plt.legend(title='Languages')
plt.show()
#-----
##create dataframe
data={'one':pd.Series([1,2,3],index=['a','b','c']),
      'two':pd.Series([10,20,30],index=['a','b','c'])}

df=pd.DataFrame(data)
print(df)

#df.plot.bar(y= year.columns[i])
df.plot.bar(y='one',x='two')
plt.show()

#df['Year'].plot.bar()







