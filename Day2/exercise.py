import array
import numpy as np

# 1. Create an array and traverse.
def traverse(array):
    for el in array:
        print(el)

# 2. Access individual elements through indexes
def accessThroughIndex(array, index):
    print(array[index])

# 3. Append any value to the array using append() method
def appendToArray(array, value):
    array.append(value)

# 4. Insert value in an array using insert() method
def insertToArray(array, value):
    # insert to first 0 insert to last 1
    array.insert(0, value)

# 5. Extend python array using extend method
def extendArray(array, newArray):
    array.extend(newArray)

# 6. Add items from list into array using fromlist() method
def addItems(array, items):
    array.fromlist(items)

# 7. Remove any array element using remove() method
def removeArray(array, value):
    array.remove(value)

# 8. Remove last array element using pop() method
def removeLastOfArray(array):
    array.pop()

# 9. Fetch any element through its index using index() method
def findIndex(array, value):
    return array.index(value)

# 10. Reverse a python array using reverse() method
def reverseArray(array):
    array.reverse()

# 11. Get array buffer information through buffer_info() method
def bufferInfoArray(array):
    return array.buffer_info()

# 12. Check for number of occurrences of an element using count() method
def countInArray(array, value):
    return array.count(value)

# 13. Convert array to string using toString() method
def convertString(array):
    resultStr = ""
    for el in array:
        resultStr += str(el)
    return resultStr

# 14. Convert array to a python list with same elements using tolist() method
def convertList(array):
    return array.tolist()

# 15. Append a string to char array using fromstring() method
def appendStrongToCharArray(array, tmpStr):
    return np.append(array, [tmpStr], axis=0)

# 16. Slice Elements from an array
def sliceArray(array, firstEl, lastEl):
    return array[firstEl:lastEl]


#--------------------------------------------------------
# Test here