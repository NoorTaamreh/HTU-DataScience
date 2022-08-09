# import numpy as np
# import mnist
# from tensorflow import keras
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
# from tensorflow.keras.utils import to_categorical

# train_images=mnist.train_images() #load the training images
# train_labels=mnist.train_labels() #load the training labels
# test_images=mnist.test_images() #load the test images
# test_labels=mnist.test_labels() #load the test labels

# # print(train_images.shape) #train_images is a numpy array of shape (60000,28,28)
# #using the 28x28 images of the mnist dataset to train the model
# #print(train_labels.shape) 
# #train_labels is a numpy array of shape (60000,1) containing the labels of the training data

# train_images=(train_images/255)-0.5 #normalize the images to be between -0.5 and 0.5
# test_labels=(test_labels/255)-0.5 #normalize the images to be between -0.5 and 0.5

# #print(train_images) #print the normalized training images

# train_images=np.expand_dims(train_images,axis=3) #add a dimension to the images to make them 3 dimensional (28x28x1)
# test_images=np.expand_dims(test_images,axis=3) #add a dimension to the images to make them 3 dimensional (28x28x1)

# num_filters=8 #number of filters in the convolutional layer
# filter_size=3 #size of the filter
# pool_size=2 #size of the pooling window

# #create a sequential model
# model=Sequential([ 
#     Conv2D(num_filters,filter_size,input_shape=(28,28,1)),
#     MaxPooling2D(pool_size),
#     Flatten(),
#     Dense(10,activation='softmax')
# ])

# model.compile('adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# model.fit(train_images,to_categorical(train_labels),epochs=3,validation_data=(test_images,to_categorical(test_labels)))
# model.summary() #print the model summary
#inthis code issue during the training of the model, the model is not able to train properly.
#----------------

#Eng Yazan Code:
import numpy as np
import mnist
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical

train_images = mnist.train_images()
train_labels = mnist.train_labels()
test_images = mnist.test_images()
test_labels = mnist.test_labels()

train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5

train_images = np.expand_dims(train_images, axis = 3)
test_images = np.expand_dims(test_images, axis = 3)

num_filters = 8
filter_size = 3
pool_size = 2

model = Sequential([ 
    Conv2D(num_filters, filter_size, input_shape = (28,28,1)),
    MaxPooling2D(pool_size),
    Flatten(),
    Dense(10, activation = 'softmax')
])

model.compile('adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# model.fit(train_images, to_categorical(train_labels), epochs = 3, validation_data=(test_images,to_categorical(test_labels)))

# model.save_weights('weights.h5') #save the weights of the model first step
#you must comment out the above line model.fit() and madel.save_weights() to run the below line
 
#load the weights of the model
model.load_weights('weights.h5')

#predect on the first 5 test images
predictions = model.predict(test_images[:20])

#print the predictions
print(np.argmax(predictions, axis = 1)) 
print(test_labels[:20]) #print the labels of the test images to compare with the predictions

#to check the accuracy of the model
