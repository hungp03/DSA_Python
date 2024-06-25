def Nhan(a, b):
    num_a = int(''.join(map(str, a)))
    num_b = int(''.join(map(str, b)))
    
    if num_a * num_b > 2**32 - 1:
        return [-1] * len(a)
    else:
        return num_a * num_b

a = [1, 2, 3]
b = [4, 5, 6]
result = Nhan(a, b)
print(result)
