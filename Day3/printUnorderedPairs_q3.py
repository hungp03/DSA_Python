def printUnorderedPairs(lst):
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            print(str(lst[i]) + "," + str(lst[j]))

lst = [1,2,3]
printUnorderedPairs(lst)