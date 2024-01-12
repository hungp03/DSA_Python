def fibonacci(n):
    if n <= 0:
        print("n phải là số nguyên dương")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Số fibonacci thứ 5 là",fibonacci(5))



