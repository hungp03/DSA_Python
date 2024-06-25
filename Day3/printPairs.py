def printPairs(lst):
    for el1 in lst:
        for el2 in lst:
            print(str(el1) + "," + str(el2))

printPairs(list([2,3,4]))