from array import array
    
def foo(array):
    sum = 0
    product = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print("Sum = " + str(sum) + ", Product = " + str(product))

testArray = array('i', [1,2,3,4,5,6,7,8,9])
foo(testArray)