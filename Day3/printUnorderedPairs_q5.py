
def printUnorderedPairs(lstA, lstB):
    for i in lstA:
        for j in lstB:
            for k in range(0,100000):
                print(str(i) + "," + str(j))

listA = [1,2,3,4,5]
listB = [6,7,8,9,10]
printUnorderedPairs(listA,listB)