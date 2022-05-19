import tensorflow as tf

# index, Date, Close/Last, Volume, Open, High, Low


import pandas as pd
import numpy as np

datafile = pd.read_csv(r"./AppleStockData.csv")
datafile = datafile.drop(columns="Open")

def configureData(data):
    data["Close/Last"] = data["Close/Last"].apply(lambda x: float(x.strip("$")))
    data["High"] = data["High"].apply(lambda x: float(x.strip("$")))
    data["Low"] = data["Low"].apply(lambda x: float(x.strip("$")))
def getTrain(data, target):
    train = np.flipud(data.loc[target+1:target+30, ["Close/Last", "Volume",  "High", "Low"]].to_numpy())#flip and convert to float for number vals
    return train
def getLabel(data, target):
    label = data.iloc[0]["Close/Last"]
    return label

configureData(datafile)
trainData = getTrain(datafile, 0)
lables = getLabel(datafile, 0)
normalizer = tf.keras.layers.Normalization(axis=-1)
normalizer.adapt(trainData)
print(normalizer.mean.numpy())