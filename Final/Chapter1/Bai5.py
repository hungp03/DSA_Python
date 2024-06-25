def sum_divisors(n):
    sum = 0
    for i in range(1, int(n*0.5) + 1):
        if n % i == 0:
            sum += i
    return sum

def Number(n):
    s = sum_divisors(n)
    if s < n:
        return "deficient"
    elif s == n:
        return "perfect"
    else:
        return "abundant"
    
if __name__ == "__main__":
    x = None
    y = None

    while True:
        x = int(input("x = "))
        y = int(input("y = "))
    
        if y >= x:
            break
        else:
            print("Yêu cầu x <= y. Vui lòng nhập lại.")

    for i in range(x, y + 1):
        print(f'{i}: {Number(i)}')
