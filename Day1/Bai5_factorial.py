def factorial(n):
    assert isinstance(n, int) and n >= 0, "Error: n phải là một số nguyên không âm"
    if n == 0:
        return 1
    return n * factorial(n-1)

print("5! =",factorial(5))