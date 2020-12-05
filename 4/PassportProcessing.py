import os
import string, sys
import re

haircolour = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

class passportData(object):
    def __init__(self):
        self.data = {}

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
    data = []
    newdata = []
    index = ''
    passportdata = passportData()
    for line in input:
        #check if line is not equal to empty
        val = line
        while (1) :
            if line.startswith("\n"):
                if (("cid" in  passportdata.data) and (len(passportdata.data) == 8)) or (("cid" not in  passportdata.data) and (len(passportdata.data) == 7)):
                    data.append(passportdata)
                    if (1920 <= int(passportdata.data.get('byr'))) and (2002 >= int(passportdata.data.get('byr'))) :
                        if (2010 <= int(passportdata.data.get('iyr'))) and (2020 >= int(passportdata.data.get('iyr'))) :
                            if (2020 <= int(passportdata.data.get('eyr'))) and (2030 >= int(passportdata.data.get('eyr'))) :
                                if passportdata.data.get('ecl') in haircolour :
                                    pattern = re.compile("[a-f0-9]+")
                                    for pos, char in enumerate(passportdata.data.get('hcl')):
                                        if pos >= 1 :
                                            if (pattern.fullmatch(char)):
                                                correct = 1
                                                pass
                                            else:
                                                correct = 0
                                                break
                                    if (pos == 6) and (correct == 1) :
                                        if len(passportdata.data.get('pid')) == 9 :
                                            height = passportdata.data.get('hgt')
                                            if height.endswith("cm"):
                                                value = height.replace('cm', '')
                                                if (int(value) <= 193) and (int(value) >= 150):
                                                    newdata.append(passportdata)
                                            else:
                                                if height.endswith("in"):
                                                    value = height.replace('in', '')
                                                    if (int(value) <= 76) and (int(value) >= 59):
                                                        newdata.append(passportdata)
                passportdata = passportData()
                break

            else:
                if (not(' ' in val)):
                    key, value = writeData(val)
                    passportdata.data[key]= value
                    if val.endswith("\n"):
                        break
                    val = line
                else:
                    val, line = split_line(line, ' ', 1)
                    if line.endswith("\n") and (not(' ' in line)):
                        key, value = writeData(val)
                        passportdata.data[key]= value
                        key, value = writeData(line)
                        passportdata.data[key]= value
                        break
    return data, newdata

def writeData(value):
    Id, val = split_line(value, ':', 1)
    val=val.strip()
    return Id, val


#####################################
#            Main Section           #
#####################################

if __name__ == "__main__":
    print("Program execution begins here")
    #get array information
    input = []
    outputData = []
    outputNewData = []

    #extract array from input
    input = readfile(["PassportProcessing.txt"])
    outputData, outputNewData = interpretData(input)
    print("valid passwords puzzle 1 is {0}" .format(len(outputData)))
    print("valid passwords puzzle 2 is {0}" .format(len(outputNewData)))