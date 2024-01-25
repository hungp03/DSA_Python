def reverse(lst):
    for i in range(0, int(len(lst)/2)):
        other = len(lst)-i-1
        temp = lst[i]
        lst[i] = lst[other]
        lst[other] = temp
    print(lst)

lst = [1, 2, 3, 4, 5]
reverse(lst)
