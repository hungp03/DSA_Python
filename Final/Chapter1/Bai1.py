def Fibonacci(n):
    if n < 0: 
        return False
    if n == 0 or n == 1:
        return True
    a, b = 0, 1
    while True:
        c = a + b
        if c == n:
            return True
        elif c > n:
            return False
        a, b = b, c


def FibonacciRecusion(n, a=0, b=1):
    if n < 0:
        return False
    elif n == 0:
        return True
    elif b < n:
        return FibonacciRecusion(n, b, a + b)
    elif b == n:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input("Nhập số nguyên cần kiểm tra: "))
    res = Fibonacci(n)
    # res = FibonacciRecusion(n)
    print(n, "là số Fibonacci") if res else print(n, "không là số Fibonacci")
