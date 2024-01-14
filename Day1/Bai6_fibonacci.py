def fibonacci(n):
    assert isinstance(n, int) and n > 0, 'n phải là số nguyên dương'
    # First Fibonacci number is 0
    if n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Số fibonacci thứ 5 là",fibonacci(5))



