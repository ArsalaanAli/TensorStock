# import tensorflow as tf

# index - date - close - volume - open - high - low

import pandas as pd

datafile = pd.read_csv(r"./AppleStockData.csv")
datafile = datafile.drop(columns="Open")

def getPastThreeMonths(data):
    endIndex = 0
    startDate = data.iloc(0)[0]["Date"]
    startMonth = int(startDate[0:2])
    for row in data.iterrows():
        curMonth = int(row[1]["Date"][0:2])
        if curMonth < startMonth - 2:
            break
        print(curMonth)
        endIndex += 1
    return endIndex
print("end", getPastThreeMonths(datafile))