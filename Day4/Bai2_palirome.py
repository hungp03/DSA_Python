# Time complexity: O(N/2) => Bỏ qua hằng số => O(N) vói N = len(s)
def isPalirome(s):
    # return s == s[::-1]
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

print(isPalirome('abba'))
print(isPalirome('abcd'))