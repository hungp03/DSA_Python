def Tru(a,b):
    len_diff = len(a) - len(b)
    if len_diff > 0:
        b = [0] * len_diff + b
    else:
        a = [0] * abs(len_diff) + a

    res = []
    tmp = 0

    for i in range(len(a) - 1 , -1, -1):
        da = a[i]
        db = b[i]

        if da < db + tmp:
            da += 10
            tmp = 1
        else:
            tmp = 0
        df = da - db - tmp
        res.insert(0, df)

    while res[0] == 0 and len(res) > 1:
        res.pop(0)

    return res

# Kiểm tra phương thức Tru()
a = [1, 2, 3]
b = [4, 5, 6]
print("a - b:", Tru(a, b))

c = [9, 9, 9]
d = [1, 1, 1]
print("c - d:", Tru(c, d))    