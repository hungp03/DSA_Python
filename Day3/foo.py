def foo(lst):
    sum = 0
    product = 1
    for i in lst:
        sum += i;
        product *= i;
    print("Sum = " + str(sum) + ", Product = " + str(product))

testList = [1,2,3,4,5,6,7,8,9]
foo(testList)
