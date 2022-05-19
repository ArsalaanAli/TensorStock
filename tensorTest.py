# import tensorflow as tf

# index, Date, Close/Last, Volume, Open, High, Low

import pandas as pd
import numpy as np

datafile = pd.read_csv(r"./AppleStockData.csv")
datafile = datafile.drop(columns="Open")

def getTrainAndLabel(data, target):
    train = data.loc[target+1:target+30, ["Date", "Close/Last", "Volume",  "High", "Low"]].to_numpy() #flip and convert to float for number vals
    label = float(data.iloc[0]["Close/Last"].strip("$"))
    return [train, label]
print(getTrainAndLabel(datafile, 0))
