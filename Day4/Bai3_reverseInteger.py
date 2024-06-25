# Time complexity: O(logN) với N = abs(n)
def reverseInteger(n):
    try:
        flag = 1 if n >= 0 else -1
        res = 0
        n = abs(int(n))
        while n > 0:
            d = n % 10
            res = res * 10 + d
            n //= 10
        return res * flag
    except ValueError:
        return 'n must be integer'

# print(reverseInteger(1234)) => Output: 4321
# print(reverseInteger(-1234)) => Output: -4321
    
inp = int(input("Enter the number to reverse: "))
print(reverseInteger(inp))