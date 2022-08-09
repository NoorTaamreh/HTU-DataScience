#to find the no of the flips pages in the given sequence of pages
#2 the shortest path for page to start from the bigginning or end of the book

#1
def flip_page(page):
    if page %2 ==0:
        flip=page/2
    else:  
        page -=1
        flip=page/2
    return flip

x=flip_page(72)
print(x) 



#----------
from sklearn.neighbors import KNeighborsClassifier # Importing the KNeighborsClassifier to use it
from sklearn.model_selection import train_test_split # Importing the train_test_split to split the data into train and test
from sklearn.datasets import load_digits
# Importing the load_digits to load the data from the digits dataset and 
# to use it for training and testing the model with the data 

digits = load_digits() # Loading the data from the load_digits 
x = digits.data # Assigning the data to the x
y = digits.target # Assigning the target to the y (the target is the digit - 0 to 9 = labels)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=40, stratify=y)
# Splitting the data into training and testing data
# test_size is the percentage of the data that will be used for testing
# random_state is the seed used by the random number generator
#stratify is used to make sure that the data is split in the same way every time

knn = KNeighborsClassifier(n_neighbors=7) # Creating a KNeighborsClassifier object with n_neighbors=7

knn.fit(x_train, y_train) # Fitting the data to the KNeighborsClassifier

print(knn.score(x_test, y_test)) # Printing the score of the KNeighborsClassifier
# The score is the accuracy of the model
    