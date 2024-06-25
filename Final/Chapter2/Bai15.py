def DayConDaiNhat(a, b):
    len_a = len(a)
    len_b = len(b)
    
    for i in range(len_a):
        for j in range(len_b):
            if a[i] == b[j]:
                subseq = [a[i]]
                for k in range(1, min(len_a - i, len_b - j)):
                    if a[i + k] == b[j + k]:
                        subseq.append(a[i + k])
                    else:
                        break
                if len(subseq) > 1:
                    return subseq
    return []

a = [1, 6, 2, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 5, 3, 7, 8]
print(DayConDaiNhat(a,b))