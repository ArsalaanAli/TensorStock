from DataExtractFunctions import *
'''
for i in range(1, 22):
    print(i, "done")
    csv = openCsv("STOCKDATA ({})".format(i))
    for j in range(0, len(csv)-30, 30):
        train = getTrain(csv, j)
        label = getLabel(csv, j)
        addArrayToTrainData(train)
        addArrayToLabelData(label)
'''
loadFile = open("trainData.npy", "rb")
tmp = np.load(loadFile)
loadFile1 = open("labelData.npy", "rb")
tmp1 = np.load(loadFile1)
print(len(tmp))
print("================================================")
print(len(tmp1))