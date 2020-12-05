import os
import string, sys

class arrayinfo(object):
    def __init__(self, passcode='', letter=''):
        self.passcode = passcode
        self.letterindex = []
        self.letter = ''
        self.min = 0
        self.max = 0
        self.occurance = 0

#water flow module
#get array information
def readfile(files):
    input = []
    for f in files:
        input = input + open(f).readlines()
    return input

def split_line(line, stype, number):
    upper = line.split(stype, number)[0]
    lower = line.split(stype, number)[1]
    return upper, lower

def interpretData(input):
    array_oldpolicy = []
    array_newpolicy = []
    for line in input:
        arraydata = arrayinfo()
        linestrip=line.strip()
        #store min value
        arraydata.min, temp = split_line(linestrip, '-', 1)
        arraydata.max, temp = split_line(temp, None, 1)
        arraydata.letter, arraydata.passcode = split_line(temp, ':', 1)
        arraydata.passcode = arraydata.passcode.strip()
        arraydata.occurance = arraydata.passcode.count(arraydata.letter)
        if (arraydata.occurance >= int(arraydata.min)) and (arraydata.occurance <= int(arraydata.max)):
            array_oldpolicy.append(arraydata)

        for pos, char in enumerate(arraydata.passcode):
            if char == arraydata.letter :
                arraydata.letterindex.append(pos+1)
        count = 0
        for val in arraydata.letterindex:
            if val == int(arraydata.min):
                count = count + 1
            if val == int(arraydata.max):
                count = count + 1
        if count == 1 :
            array_newpolicy.append(arraydata)

        pass

    print(" old policy valid passwords are {0}" .format(len(array_oldpolicy)))
    print(" new policy valid passwords are {0}" .format(len(array_newpolicy)))




#####################################
#            Main Section           #
#####################################

if __name__ == "__main__":
    print("Program execution begins here")
    #get array information
    input = []

    #extract array from input
    input = readfile(["PasswordPhilosophy.txt"])
    interpretData(input)

    pass