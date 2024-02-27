def sum_product(tple):
    sum, product = 0, 1
    for i in tple:
        sum += i
        product *= i
    return sum, product

input_tuple = (1,2,3,4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)