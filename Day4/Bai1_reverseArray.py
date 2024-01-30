# Time complexity: O(N/2) => Bỏ qua hằng số => O(N) với N = len(arr)
def reverseArray(arr):
    #Gắn start = 0, end = len -1
    start, end = 0, len(arr)-1

    #Hoán đổi các cặp vị trí
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr

arr = [1,2,3,4,5]
print(reverseArray(arr))
