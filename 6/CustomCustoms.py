import os
import string, sys

class customs(object):
    def __init__(self, numberOfPeople = 0 ):
        self.numberOfPeople = numberOfPeople
        self.numberOfQuestions = 0
        self.charOccurance = {}


#water flow module
#get array information
def readfile(files):
    input = []
    for f in files:
        input = input + open(f).readlines()
    return input

def interpretData(input):
    output = []
    i = 1
    customsData = customs()
    charTable = []
    total = 0
    allanswered= 0
    for line in input:
        if line.startswith("\n"):
            i = 1
            charTable = []
            total = total + customsData.numberOfQuestions
            for key, value in customsData.charOccurance.items():
                if int(value) == customsData.numberOfPeople :
                    allanswered = allanswered + 1
            output.append(customsData)
            customsData = customs()
        else:
            line = line.strip()
            for char in line:
                customsData.numberOfPeople = i
                if char not in charTable:
                    customsData.numberOfQuestions = customsData.numberOfQuestions + 1
                    charTable.append(char)
                    customsData.charOccurance[char] = 1
                else:
                    customsData.charOccurance[char] = customsData.charOccurance[char] +1


            i = i + 1

    return output, total, allanswered


#####################################
#            Main Section           #
#####################################

if __name__ == "__main__":
    print("Program execution begins here")
    #get array information
    input = []
    output = []
    total = 0
    allanswered = 0
    #extract array from input
    input = readfile(["CustomCustoms.txt"])
    output, total, allanswered = interpretData(input)
    print("all questions count is {0}" .format(total))
    print("all commonly answered yes question is {0}" .format(allanswered))