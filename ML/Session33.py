# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib as plt
# import matplotlib.pyplot as plt
# from sklearn.datasets import load_breast_cancer
# from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA

# cancer=load_breast_cancer() 
# df= pd.DataFrame(data=cancer.data,columns=cancer.feature_names)

# print(df.head(5)) #print first 5 rows
# #print(df) #print all the data
# #print(df.info()) #print the info of the dataframe

# #the first step you must preprocess the data
# #standardize the data
# #we need to standardize the data so that it has a mean of 0 and a standard deviation of 1
 
# X=df.values #convert the dataframe to a numpy array

# #create a scaler object
# scaler=StandardScaler()

# #calculate the mean and standard deviation of the data
# scaler.fit(X)

# #transform the data
# X_Scaled=scaler.transform(X)

# #create your model 
# pca_30=PCA(n_components=3,random_state=2020)
# pca_30.fit(X_Scaled)
# output=pca_30.transform(X_Scaled)

# #to know each features how its effect the result
# # print(pca_30.explained_variance_ratio_ *100)

# # print(np.cumsum(pca_30.explained_variance_ratio_ *100))


# plt.figure(figsize=(10,7))
# sns.scatterplot(x=output[:,0],y=output[:,1],hue=cancer.target,palette=["green","blue"])
# plt.title("2 principle components")
# plt.xlabel("PC1")
# plt.ylabel("PC2")
# plt.show()
# # plt.savefig("2_principle_components.png")

# from mpl_toolkits import mplot3d
# plt.figure(figsize=(10,7))
# ax=plt.axes(projection="3d")
# sctt=ax.scatter3D(output[:,0],output[:,1],output[:,2],c=cancer.target,s=50,alpha=0.5)
# plt.title("3 principle components")
# ax.set_xlabel("PC1")
# ax.set_ylabel("PC2")
# ax.set_zlabel("PC3")
# plt.show()

#-------------

import numpy as np
import matplotlib.pyplot as plt

#create evenly spaced numbers over a specified interval
x=np.linspace(-5,5,100)
z=1/(1+np.exp(-x))

#visualize the sigmoid function
plt.plot(x,z)
plt.xlabel("x")
plt.ylabel("z")
plt.show()