#unsupervised
from sklearn import datasets
from matplotlib import pyplot as plt

df=datasets.load_iris()
#print the features of the dataframe
print(df.feature_names)

#print target names = labels of the dataframe
print("target_names",df.target_names)
print(df.target)


label={0:'red',1:'blue',2:'green'} 
#create a dictionary to map the labels to colors and names (for each cluster)
#even you common out the line above it doesn't effect on  the result

X=df.data[:,0] #sepal length
Y=df.data[:,2] #petal length

plt.scatter(X,Y,c=df.target) #c is the color of the points
plt.show()