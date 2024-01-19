from array import array
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]), end ='\t')

arrA = array('i', [1,2,3,4,5])
arrB = array('i', [6,7,8,9,10])
printUnorderedPairs(arrA, arrB)