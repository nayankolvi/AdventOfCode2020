import os
import string, sys

class areaInfo(object):
    def __init__(self, lineData=''):
        self.lineData = lineData
        self.square = []
        self.tree = []
        self.maxcount = 0
        self.repeatPattern = 'no'

#water flow module
#get array information
def readfile(files):
    inputData = []
    for f in files:
        inputData = inputData + open(f).readlines()
    return inputData

def interpretData(inputData):
    arrayData = []
    for line in inputData:
        areainfo = areaInfo()
        linestrip=line.strip()
        areainfo.lineData = linestrip
        #get coordinates of squares and trees
        for pos, char in enumerate(linestrip):
            if char == '#' :
                areainfo.tree.append(pos+1)
            else :
                areainfo.square.append(pos+1)
            areainfo.maxcount = pos+1

        arrayData.append(areainfo)
    return arrayData

def calculateTrees(arr, right, down):
    right_val = right + 1
    down_val = down
    count = 0
    while down_val < len(arr) :
        if right_val > arr[down_val].maxcount :
            right_val = right_val - arr[down_val].maxcount
        if right_val in arr[down_val].tree :
            count = count + 1
        right_val = right_val + right
        down_val = down_val + down

    return count

#####################################
#            Main Section           #
#####################################

if __name__ == "__main__":
    print("Program execution begins here")
    #get array information
    inputData = []
    data = []
    #extract array from inputData
    inputData = readfile(["TobogganTrajectory.txt"])
    data = interpretData(inputData)
    val1 = calculateTrees(data, 3, 1)
    val2 = calculateTrees(data, 1, 1)
    val3 = calculateTrees(data, 5, 1)
    val4 = calculateTrees(data, 7, 1)
    val5 = calculateTrees(data, 1, 2)
    print("Number of trees encountered for slope {0}" .format(val1))
    print("trees encountered on listed slope {0}" .format(val1*val2*val3*val4*val5))