def decToBin(decimal):
    if decimal == 0:
        return 0
    else:
        return decimal % 2 + 10 * decToBin(int(decimal //2))

print(decToBin(12))







