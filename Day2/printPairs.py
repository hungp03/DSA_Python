from array import array
def printPairs(array):
    for i in array:
        for j in array:
            print(str(i) + "," + str(j))


printPairs(array('i', [2, 3, 4]))