import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense , SimpleRNN


n = 1000
tp = 800

t = np.arange(0,n)
x = np.sin(0.02*t) + 2*np.random.randn(n)

df = pd.DataFrame(x)

values = df.values
train , test = values[0:tp, :], values[tp:n, :]

step = 4
test = np.append(test, np.repeat(test[-1,], step))
train = np.append(train, np.repeat(train[-1,], step))

def converttomatrix(data, step):
     x, y = [], []
     for i in range(len(data) - step):
         d = i + step
         x.append(data[i:d,])
         y.append(data[d])
     return np.array(x), np.array(y)


trainx , trainy = converttomatrix(train, step)
testx , testy = converttomatrix(test,step)

trainx = np.reshape(trainx, (800, 1, 4))
testx = np.reshape(testx, (200, 1 , 4))

model = Sequential()
model.add(SimpleRNN(units=32, input_shape=(1,4), activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='rmsprop')
model.summary()

model.fit(trainx, trainy, epochs=100, batch_size=16, verbose=2)
trainpred= model.predict(trainx)
testpred= model.predict(testx)


# trainpred = model.predict(trainx)
# testpred = model.predict(testx)

#pred = np.concatenate((trainpred, testpred), axis = 0)
trainscore = model.evaluate(trainx, trainy)
print(trainscore)
# index = df.index.values
# plt.plot(index, values)
# plt.plot(index, pred)
# plt.axvline(df.index[tp], c='r')
# plt.show()
