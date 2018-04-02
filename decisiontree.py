from __future__ import division
from math import log
from collections import Counter
import pandas as pd

dataset = [['Youth', 'High', 'No', 'Fair', 'No'], ['Youth', 'High', 'No', 'Excellent', 'No'],
           ['Middle_Aged', 'High', 'No', 'Fair', 'Yes'], ['Senior', 'Medium', 'No', 'Fair', 'Yes'],
           ['Senior', 'Low', 'Yes', 'Fair', 'Yes'], ['Senior', 'Low', 'Yes', 'Excellent', 'No'],
           ['Middle_Aged', 'Low', 'Yes', 'Excellent', 'Yes'], ['Youth', 'Medium', 'No', 'Fair', 'No'],
           ['Youth', 'Low', 'Yes', 'Fair', 'Yes'], ['Senior', 'Medium', 'Yes', 'Fair', 'Yes'],
           ['Youth', 'Medium', 'Yes', 'Excellent', 'Yes'], ['Middle_Aged', 'Medium', 'No', 'Excellent', 'Yes'],
           ['Middle_Aged', 'High', 'Yes', 'Fair', 'Yes'], ['Senior', 'Medium', 'No', 'Excellent', 'No']]

dataframe = pd.DataFrame(data=dataset)


def getLogValue(p):
    sum = 0.0
    for i in p.values():
        i = i / 14.0
        sum += i * log(i, 2)
    return sum * -1


def getCounts(i):
    yesNoDict = dict()
    for j in range(0, len(dataframe[i])):
        key = dataframe[i][j]
        if key in yesNoDict.keys():
            if dataframe.iat[j,4] == 'Yes':
                yesNoDict[key][1] += 1
            else:
                yesNoDict[key][0] += 1
        else:
            if dataframe.iat[j,4] == 'Yes':
                yesNoDict[key] = [0, 1]
            else:
                yesNoDict[key] = [1, 0]
    return yesNoDict


def getGainValue(Info, yesNoDict):
    sum = 0.0
    print(yesNoDict)
    for i in yesNoDict:
        temp = 0.0
        denominator = reduce(lambda a, b: a + b, yesNoDict[i])
        for j in yesNoDict[i]:
            if j == 0:
                continue
            p = j / denominator
            temp += -p * log(p, 2)
        temp *= denominator / 14.0
        sum += temp
    return Info - sum


def iterateDecisionTree(Info):
    for i in range(0, 4):
        yesNoDict = getCounts(i)
        gain = getGainValue(Info, yesNoDict)
        print(gain)



if __name__ == '__main__':
 print("Running Decision Tree ID3 Algorithm On AllCustomers Dataset...")
print("Calculating Info(D)...")
count = Counter(dataframe[4])
print(count)
Info = getLogValue(count)
print(Info)
iterateDecisionTree(Info)

