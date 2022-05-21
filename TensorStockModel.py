import tensorflow as tf
import numpy as np

def build_model(train_data, ):    
    normalizer = tf.keras.layers.Normalization(axis=-1)
    normalizer.adapt(train_data)
    model = tf.keras.Sequential([normalizer, tf.keras.layers.Dense(64, activation='relu'),
      tf.keras.layers.Dense(64, activation='relu'),
      tf.keras.layers.Dense(1)
  ])
    model.compile(loss='mean_absolute_error',
                optimizer=tf.keras.optimizers.Adam(0.001))
    return model

# train = model.fit(trainData, labelData, epochs=1, verbose=1, )
