#1 #importing the libraries
import matplotlib.pyplot as plt
import numpy as np
import random
from tensorflow.keras.models import Sequential
#we imoprt sequential because we are building a sequential model
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D ,Dropout ,BatchNormalization
from tensorflow.keras import layers

#dense is a fully connected layer
#conv2d is a convolutional layer used to extract features from the input image
# and then use them to create a new image
#flatten is used to convert the 2D image to a 1D vector
#maxpooling is used to reduce the size of the image

#2 #importing the dataset
print("importing the dataset")
x_train=np.loadtxt('input.csv',delimiter=',') #importing the training data
y_train=np.loadtxt('labels.csv',delimiter=',') #importing the training labels
x_test= np.loadtxt("input_test.csv",delimiter=',') #importing the test data
y_test= np.loadtxt("labels_test.csv",delimiter=',') #importing the test labels
#we use loadtxt to import the data and labels from the csv files
#delimiter is used to specify the delimiter used in the csv file which is a comma

print("reshape the data")
#reshape the data to fit the model
x_train=x_train.reshape(len(x_train),100,100,3)
y_train=y_train.reshape(len(y_train),1)
x_test=x_test.reshape(len(x_test),100,100,3)
y_train=y_train.reshape(len(y_train),1)
#we use reshape to reshape the data to fit the model
#len(x_train) is the number of training images
#100,100 is the size of the image
#3 is the number of channels of the image (RGB)

print("Normalizing")
#normalizing the data to fit the model (0-1)
x_train=x_train/255.0
y_train=y_train/255.0
x_test=x_test/255.0
y_test=y_test/255.0

print("show random image")
#show random image from the training data
index=random.randint(0,len(x_train))
plt.imshow(x_train[index,:])
plt.show()


print("create the model")
#creating the model
#we create a sequential model
model=Sequential()
model.add(Conv2D(32,(3,3),activation='relu',input_shape=(100,100,3)))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Dropout(0.5)) #add dropout to avoid overfitting
model.add(BatchNormalization()) #add batch normalization to the model to avoid overfitting

model.add(Flatten())
model.add(Dense(64,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(x_train,y_train,epochs=5 ,batch_size=64)

#evaluate the model and see the accuracy
print("evaluate the model")
print(model.evaluate(x_test,y_test))


#make a prediction
print("make a prediction")

index2=random.randint(0,len(y_test))
plt.imshow(x_test[index2,:])
plt.show()

y_prediction=model.predict(x_test[index2,:].reshape(1,100,100,3))
print("value of y_prediction:",y_prediction)

y_prediction= y_prediction > 0.5
#we use > 0.5 to convert the prediction to boolean values 

if(y_prediction == 0):
    prd="Dog"
else:
    prd="Cat"
    
print("The model predict, this is a "+ prd)