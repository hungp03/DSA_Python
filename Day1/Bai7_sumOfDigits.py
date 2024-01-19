def sumOfDigits(n):
    assert isinstance(n, int), 'n phải là số nguyên'
    if n < 0:
        return sumOfDigits(abs(n))
    if n == 0:
        return 0
    return (n % 10) + sumOfDigits(n //10)


print(sumOfDigits(-123))