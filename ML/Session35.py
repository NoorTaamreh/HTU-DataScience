import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation ,Flatten

model=Sequential()
#sequential model is a linear stack of layers (input layer, hidden layer, output layer)
#is used to create a model that is linear in nature
#Step 1: Add the input layer and the first hidden layer using the add() method

layer1=Dense(8,input_shape=(4,))
#define the number of nodes in the layer and the shape of the input data
#8 nodes in the first hidden layer and the input shape is 4x1 (4 features and 1 sample)
#the no of layer in this case is 1

model.add(layer1)

layer2=Flatten()
#flatten the input data to a 1D array of values
#it has no input shape and no input dimension (because it is a flatten layer)

model.add(layer2)

model.summary()


#--------------

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

y_true = [3, -0.5, 2,7]
y_perd=[12.5,10,20,100]

print(mean_absolute_error(y_true,y_perd))

#you can do this operation using numpy
#np.sqrt() which is to find the square root for the number

#-------------
