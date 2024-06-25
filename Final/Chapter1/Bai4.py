def Pascal(n):
    assert n > 0, "n phải là số nguyên dương"
    pascal = [[0] * (i+1) for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(i+1):
            if j == 0 or j == i:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    for i in range(n + 1):
        print("n=" + str(i), end=" ")
        for j in range(i+1):
            print(pascal[i][j], end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Nhập số nguyên dương n: "))
    Pascal(n)
