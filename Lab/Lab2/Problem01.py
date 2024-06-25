def sliding_window_max(nums, k):
    if k <= 0 or k > len(nums):
        return "Invalid input"
    
    max_nums = []
    window = []
    
    for i, num in enumerate(nums):
        if i >= k and window[0] <= i - k:
            window.pop(0)
        
        while window and nums[window[-1]] <= num:
            window.pop()
        
        window.append(i)
        
        if i >= k - 1:
            max_nums.append(nums[window[0]])
    
    return max_nums


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(sliding_window_max(num_list, k))
