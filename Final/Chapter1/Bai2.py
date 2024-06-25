def factorial_recusive(n):
    if n == 0 or n == 1:
        return 1
    return factorial_recusive(n-1) * n

def fatorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def Neper(n):
    assert n > 0, "n phải lớn hơn 0"
    e = 0
    for i in range(0, n + 1):
        e += 1/fatorial(i)
    return e

if __name__ == "__main__":
    n = int(input("N = "))
    res = Neper(n)
    print(f"Neper({n}) = {res}")