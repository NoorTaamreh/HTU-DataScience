# from sklearn.datasets import load_iris
# from sklearn.linear_model import LogisticRegression

# x, y = load_iris(return_X_y=True)  
# #return_X_y is used to return the data in the form of numpy arrays and not pandas dataframes 
# #x is the data and y is the target variable

# clf = LogisticRegression(random_state=0).fit(x, y)
# #clf is the classifier object and fit is the function 
# #used to train the classifier  on the data x and y respectively
# #random_state is used to generate the same random numbers everytime

# clf.predict(x[:2, :])
# #clf.predict(x[:2, :]) will return the predicted values for the first two rows of the data
# #[:2, :] is used to predict the first two rows of the data)

# print(clf.predict_proba(x[:2, :]))
# #clf.predict_proba(x[:2, :]) gives the probability of the target variable to be 1
# print(clf.score(x,y))
# #clf.score(x,y) gives the accuracy of the model

#-------------------
from matplotlib import cm
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
#make_blobs is used to generate the data for the classification problem 

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neural_network import MLPClassifier

(X, y) = make_blobs(n_samples=150, n_features=2, centers=2, random_state=0)
#make_blobs is used to generate the data for the classification problem
#n_samples is the number of samples in the data
#n_features is the number of features in the data
#centers is the number of clusters in the data
#random_state is used to generate the same random numbers everytime

(X_test,y_test) = make_blobs(n_samples=20, n_features=2, centers=2, random_state=10)
#X_test is the data for the test set
#y_test is the target variable for the test set

mlp = MLPClassifier(hidden_layer_sizes=(8,8,8),activation='relu',solver="adam", max_iter=500)
#hidden_layer_sizes is the number of neurons in each hidden layer which is 3 in this case 
#in each hidden layer there are 8 neurons
#activation is the activation function which is relu in this case
#solver is the solver used to solve the optimization problem 
#max_iter is the maximum number of iterations to be performed

mlp.fit(X,y)
#mlp.fit(X,y) is used to train the model on the data X and y respectively

print(mlp.predict(X))
#mlp.predict(X) gives the predicted values for the data X

print(classification_report(y_test,mlp.predict(X_test)))    
#classification_report(y_test,mlp.predict(X_test)) gives the classification report for the test set

print(confusion_matrix(y,mlp.predict(X)))
#confusion_matrix(y,mlp.predict(X)) gives the confusion matrix for the data X

#-------------------
#using nural network to classify the data in iris dataset
# from sklearn.datasets import load_iris
# from sklearn.linear_model import LogisticRegression
# (X, y) = load_iris(return_X_y=True)

# mlp=MLPClassifier(hidden_layer_sizes=(8,8,8),activation='relu',solver="adam", max_iter=500)
# mlp.fit(X,y)
# print(mlp.predict(X))
# print(classification_report(y,mlp.predict(X)))

 