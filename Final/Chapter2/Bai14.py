def DayConDauTien(a, b):
    len_a = len(a)
    len_b = len(b)
    
    for i in range(len_a):
        for j in range(len_b):

            if a[i] == b[j]:
                if i + 1 < len_a and j + 1 < len_b and a[i + 1] == b[j + 1]:
                    return [a[i], a[i + 1]]
    return []

a = [1, 6, 2, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 5, 3, 7, 8]
print(DayConDauTien(a,b))