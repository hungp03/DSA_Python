from collections import deque

def max_sliding_window(num_list, size):
    if not num_list:
        return []
    
    result = []
    window = deque()
    
    for i, num in enumerate(num_list):
        while window and num_list[window[-1]] < num:
            window.pop()
        
        window.append(i)
        
        if i - window[0] >= size:
            window.popleft()
        
        if i >= size - 1:
            result.append(num_list[window[0]])
    
    return result

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
size = 3
output = max_sliding_window(num_list, size)
print(output)
