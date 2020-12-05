import os
import string, sys

#water flow module
#get array information
def readfile(files):
    input = []
    for f in files:
        input = input + open(f).readlines()
    return input

def interpretData(input):
    seatvalues = []
    missing = 0
    i = 0
    max_val = 0
    for line in input:
        row = 0
        col = 0
        ref_row = 0
        ref_col = 0
        line=line.strip()
        #store min value
        for c in reversed(line):
            if c == 'F' :
                row = pow(2, ref_row)*0 + row
                ref_row = ref_row + 1
            elif c == 'B' :
                row = pow(2, ref_row)*1 + row
                ref_row = ref_row + 1
            elif c == 'L' :
                col = pow(2, ref_col)*0 + col
                ref_col = ref_col + 1
            else :
                col = pow(2, ref_col)*1 + col
                ref_col = ref_col + 1
        
        seatvalues.append(row * 8 + col)
        if (seatvalues[i] > max_val ) :
            max_val = seatvalues[i]
        i = i + 1

    seatvalues.sort()
    for j in range(len(seatvalues)-1) :
        if seatvalues[j+1] != (seatvalues[j]+1):
            missing = seatvalues[j]+1
    return max_val, missing

#####################################
#            Main Section           #
#####################################

if __name__ == "__main__":
    print("Program execution begins here")
    #get array information
    input = []
    #extract array from input
    input = readfile(["BinaryBoarding.txt"])
    max_Seatval, yourSeat = interpretData(input)
    print("Max seats in flight is {0}" .format(max_Seatval))
    print("your seat  in flight is {0}" .format(yourSeat))