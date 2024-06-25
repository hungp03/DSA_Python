from array import array
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))

arrA = array('i', [1,2,3,4,5])
arrB = array('i', [6,7,8,9,10])
printUnorderedPairs(arrA, arrB)