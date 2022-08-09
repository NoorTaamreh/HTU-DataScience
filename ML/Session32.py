# #kmmeans clustering
# from sklearn import datasets
# from sklearn.cluster import KMeans
# from sklearn.manifold import TSNE
# import matplotlib.pyplot as plt

# #loading dataset
# IRIS_DF=datasets.load_iris()

# #defining the model
# model=KMeans(n_clusters=3)
# model.fit(IRIS_DF.data)
# predecters_labels=model.predict([[7.2,3.6,5.1,2.5]]) #one input you insert the entru for the for fetures
# print(predecters_labels) #print class  of cluster

# all_predictions=model.predict(IRIS_DF.data) #prediction ontje  entire data
# print(all_predictions)
#-------------------------
# # hierarchy CLUSTERING
# from scipy.cluster.hierarchy import linkage, dendrogram #LINKAGE is for clustering 
# #DENDOGRAM is for plotting
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# #reading the data frame
# seeds_DF=pd.read_csv("https://raw.githubusercontent.com/valeriich/ML/master/seeds-less-rows.csv")

# #remove the grain species from the data frame and save for later
# Varieties=list(seeds_DF.pop('grain_variety')) 

# #extract the measurements as anumpy array
# Samples=seeds_DF.values
# print(Samples)
# mergings=linkage(Samples,method='complete')

# dendrogram(mergings,labels=Varieties,leaf_rotation=90,leaf_font_size=7)
# #mergings is the output of the linkage function
# #labels is the name of the clusters
# #leaf_rotation is the angle of the text
# #leaf_font_size is the size of the text

# plt.show()

#-------------
#tsne clustering
from sklearn import datasets
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

#loading dataset
IRIS_DF=datasets.load_iris()

#defining the model
MODEL=TSNE(learning_rate=100) #learning_rate is the number of iterations

#fitting the model
transformed=MODEL.fit_transform(IRIS_DF.data)
#fit_transform is used to fit the model and transform the data 
# from the original space to the new space which is the 2D space
print (transformed)

#plotting 2D T-SNE
x_axis=transformed[:,0]
y_axis=transformed[:,1]

plt.scatter(x_axis,y_axis,c=IRIS_DF.target) #target is the class of the data
plt.show()