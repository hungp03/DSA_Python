# Tìm ước chung lớn nhất của x và y
def gcd(x,y):
    # Kiểm tra xem x và y có phải là số hay không
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("X và Y phải là số")
    if x == 0:
        return y
    if y == 0:
        return x
    return gcd(y, x % y)

print("GCD(15, 6) =",gcd(15,6))