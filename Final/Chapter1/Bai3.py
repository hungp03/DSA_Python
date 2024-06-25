def GCD(a, b):
    while b != 0:
        a, b = b, a % b
        # a = b
        # b = a % b
    return a

def GCD_recusive(a,b):
    if b == 0:
        return a
    return GCD_recusive(b, a%b)

if __name__ == "__main__":
    tmp = input("Nhập 2 số nguyên cách nhau bởi dấu cách: ")
    a, b = map(int, tmp.split())
    print(f"GCD({a}, {b}) = {GCD(a,b)}" )
    print(f"GCD_recusive({a}, {b}) = {GCD_recusive(a,b)}" )