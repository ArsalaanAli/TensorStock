import tensorflow as tf
import numpy as np
import pandas as pd

def build_model():
  model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, kernel_initializer='normal', activation='relu'),
    tf.keras.layers.Dense(64, kernel_initializer="normal", activation='relu'),
    tf.keras.layers.Dense(64, kernel_initializer="normal", activation='relu'),
    tf.keras.layers.Dense(1)
  ])
  model.compile(loss="mean_squared_logarithmic_error",
                optimizer=tf.keras.optimizers.Adam(0.001))
  return model

loadFile = open("trainData.npy", "rb")
train = np.load(loadFile)[0]
loadFile1 = open("labelData.npy", "rb")
label = np.load(loadFile1)[0]

train = np.array([train])
label = np.array([label])


print(train, label)

model = build_model()

trained = model.fit(train, label, epochs=1, verbose=1, )

pred = model.predict(train)

print(pred)