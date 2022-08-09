#autoencoder

import tensorflow.keras as keras
import tensorflow.keras.layers as layers
from tensorflow.keras.datasets import mnist
import numpy as np

#the size of encoded representations
encoding_dim = 32 
# 32 floats -> compression of factor 24.5, assuming the input is 784 floats
#32 no. of neurons in the hidden layer


input_img = keras.Input(shape=(784,))
#784 is the no. of pixels in the input image (28x28)
#this is the input layer of the autoencoder
#input_img is the input layer of the autoencoder

encoded = layers.Dense(encoding_dim, activation='relu')(input_img)
#the encoded layer is a fully connected layer with 32 neurons and activation function is relu


# "decoded" is the lossy reconstruction of the input
decoded = layers.Dense(784, activation='sigmoid')(encoded)
#the decoded layer is a fully connected layer with 784 neurons and activation function is sigmoid
#the output is a sigmoid layer
#encoded is the input to the decoded layer

# This model maps an input to its reconstruction
autoencoder = keras.Model(input_img, decoded)
#the autoencoder is a model that maps an input to its reconstruction
#input_img is the input to the autoencoder
#decoded is the output of the autoencoder

#----------------------------------------------------------------------------------
# This model maps an input to its encoded representation
encoder = keras.Model(input_img, encoded)
#encoder is a model that maps an input to its encoded representation (the lossy representation)

# This is our encoded (32-dimensional) input
encoded_input = keras.Input(shape=(encoding_dim,)) 
#encoded_input is the input to the decoder

# Retrieve the last layer of the autoencoder model
decoder_layer = autoencoder.layers[-1] #decoder_layer is the last layer of the autoencoder model

# Create the decoder model
decoder = keras.Model(encoded_input, decoder_layer(encoded_input))

#----------------#

autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

#--------------------------#
#loading the data
(x_train, _), (x_test, _) = mnist.load_data()


#normalizing the data
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
print(x_train.shape)
print(x_test.shape)

autoencoder.fit(x_train, x_train,
                epochs=25,
                batch_size=128,
                shuffle=True,
                validation_data=(x_test, x_test))


encoded_imgs = encoder.predict(x_test)
decoded_imgs = decoder.predict(encoded_imgs)

#--------------
# plotting the results
import matplotlib.pyplot as plt

n = 10  # How many digits we will display
plt.figure(figsize=(20, 4))
for i in range(n):
    # Display original
    ax = plt.subplot(2, n, i + 1) #2 rows, n columns, i+1 is the ith plot in the nth column
    
    plt.imshow(x_test[i].reshape(28, 28))
    plt.gray()
    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Display reconstruction
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()





