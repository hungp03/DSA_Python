# Tìm ước chung lớn nhất của x và y
def gcd(x,y):
    if x == 0:
        return y
    if y == 0:
        return x
    return gcd(y, x % y)

print("GCD(15, 6) =",gcd(1.5,6))