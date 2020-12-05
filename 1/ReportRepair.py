#water flow module
#get array information
def extract_array(myarray):
    with open('ReportRepair.txt') as f:
        #list that contains the read line
        for line in f:
            line=line.rstrip()
            myarray.append(line)


def findentries(myarray):
    result = 0
    for elem in myarray:
        for elem1 in myarray:
            for elem2 in myarray:
                result = int(elem2) + int(elem1) + int(elem);
                if result == 2020 :
                    print(int(elem1)*int(elem)*int(elem2))
                    break;
            #result = int(elem1) + int(elem);
            if result == 2020 :
                #print(int(elem1)*int(elem))
                break;
        if result == 2020 :
            break;


#####################################
#            Main Section           #
#####################################


print("Program execution begins here")
#get array information
array_information = []

#extract array from input
extract_array(array_information)
findentries(array_information)

pass