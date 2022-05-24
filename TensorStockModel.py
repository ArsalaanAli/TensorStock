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
  
  return model

def stockLoss(val_true, val_pred):
  print("THISJAHJSKFJSKFHS ==== ===================================================")
  print(val_true-val_pred)
  return val_true - val_pred

loadFile = open("trainData.npy", "rb")
train = np.load(loadFile)
loadFile1 = open("labelData.npy", "rb")
label = np.load(loadFile1)


model = build_model(train[0])
model.compile(loss=stockLoss,
                optimizer=tf.keras.optimizers.Adam(0.001))
train = model.fit(train[0:1], label[0:1], epochs=1, verbose=1, )

