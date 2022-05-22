import tensorflow as tf
import numpy as np
import pandas as pd

def build_model(train_data, ):    
    normalizer = tf.keras.layers.Normalization(axis=-1)
    normalizer.adapt(train_data)
    model = tf.keras.Sequential([normalizer, tf.keras.layers.Dense(64, activation='relu'),
      tf.keras.layers.Dense(64, activation='relu'),
      tf.keras.layers.Dense(1)
  ])
    model.compile(loss='mean_squared_logarithmic_error',
                optimizer=tf.keras.optimizers.Adam(0.001))
    return model


loadFile = open("trainData.npy", "rb")
train = np.load(loadFile)
loadFile1 = open("labelData.npy", "rb")
label = np.load(loadFile1)


model = build_model(train[0])
train = model.fit(train, label, epochs=10, verbose=1, )


# print(model.history)
# hist['epoch'] = model.epoch
# print(hist.tail())