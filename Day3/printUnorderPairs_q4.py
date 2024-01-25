def printUnorderedPairs(listA, listB):
    for i in listA:
        for j in listB:
            if i < j:
                print(str(i) + "," + str(j), end ='\t')

lstA =  [1,2,3,4,5]
lstB =  [6,7,8,9,10]
printUnorderedPairs(lstA, lstB)