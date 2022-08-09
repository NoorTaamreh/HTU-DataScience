from sklearn.neighbors import KNeighborsClassifier # Importing the KNeighborsClassifier to use it
from sklearn.model_selection import train_test_split # Importing the train_test_split to split the data into train and test
from sklearn.datasets import load_digits
# Importing the load_digits to load the data from the digits dataset and 
# to use it for training and testing the model with the data 
from sklearn import svm #importing the svm (Support vector machine) model which is used to train the data

digits = load_digits() # Loading the data from the load_digits 
x = digits.data # Assigning the data to the x
y = digits.target # Assigning the target to the y (the target is the digit - 0 to 9 = labels)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=40, stratify=y)
# Splitting the data into training and testing data
# test_size is the percentage of the data that will be used for testing
# random_state is the seed used by the random number generator
#stratify is used to make sure that the data is split in the same way every time


s= svm.SVC(kernel='poly') # Creating a SVC object with kernel='poly'

s.fit(x_train, y_train) # Fitting the data to the SVC 

print(s.score(x_test, y_test)) # Printing the score of the SVC
# The score is the accuracy of the model

#------------------------------------------------------
#linear regression
from sklearn.neighbors import KNeighborsClassifier # Importing the KNeighborsClassifier to use it
from sklearn.model_selection import train_test_split # Importing the train_test_split to split the data into train and test
from sklearn.datasets import load_digits
# Importing the load_digits to load the data from the digits dataset and 
# to use it for training and testing the model with the data 
from sklearn.linear_model import LinearRegression # Importing the LinearRegression to use it

digits = load_digits() # Loading the data from the load_digits
x=digits.data # Assigning the data to the x
y=digits.target # Assigning the target to the y (the target is the digit - 0 to 9 = labels)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=40, stratify=y)

l=LinearRegression() # Creating a LinearRegression object

l.fit(x_train, y_train) # Fitting the data to the LinearRegression
print(l.score(x_test, y_test)) # Printing the score of the LinearRegression
