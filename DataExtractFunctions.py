import pandas as pd
import numpy as np

def configureData(data):
    data["Close/Last"] = data["Close/Last"].apply(lambda x: float(x.strip("$")))
    data["High"] = data["High"].apply(lambda x: float(x.strip("$")))
    data["Low"] = data["Low"].apply(lambda x: float(x.strip("$")))
def getTrain(data, target):
    train = np.flipud(data.loc[target+1:target+3, ["Close/Last", "Volume",  "High", "Low"]].to_numpy())#flip and convert to float for number vals
    return np.array(train)
def getLabel(data, target):
    label = data.iloc[0]["Close/Last"]
    return np.array(label)
def openCsv(filename):
    datafile = pd.read_csv(r"./" + filename + ".csv")
    configureData(datafile)
    return datafile
def addArrayToTrainData(array):
    try:
        loadFile = open("trainData.npy", "rb")
        tmp = np.load(loadFile)
        tmp = np.append(tmp, array, axis=0)
        np.save("trainData", tmp)
        loadFile.close()
    except Exception as e:
        print("EXCEPTION SAVING PRINT", e)
        np.save("trainData", np.array(array))
def addArrayToLabelData(array):
    try:
        loadFile = open("labelData.npy", "rb")
        tmp = np.load(loadFile)
        tmp = np.append(tmp, np.array([array]), axis=0)
        np.save("labelData", tmp)
        loadFile.close()
    except Exception as e:
        print("EXCEPTION SAVING LABEL", e)
        np.save("labelData", np.array([array]))

'''
csv = openCsv("AppleStockData")
train = getTrain(csv, 5)
label = getLabel(csv, 0)
addArrayToTrainData(train)
addArrayToLabelData(label)
loadFile = open("trainData.npy", "rb")
tmp = np.load(loadFile)
loadFile1 = open("labelData.npy", "rb")
tmp1 = np.load(loadFile1)
print(tmp, tmp1)
'''