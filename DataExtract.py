from DataExtractFunctions import *

for i in range(1, 22):
    csv = openCsv("STOCKDATA ({})".format(i))
    print(len(csv))