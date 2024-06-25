def find_common_elements(nums1, nums2):
    count = {}
    for num in nums1:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    common_elements = []
    for num in nums2:
        if num in count and count[num] > 0:
            common_elements.append(num)
            count[num] -= 1
    
    return common_elements

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(find_common_elements(nums1, nums2))

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(find_common_elements(nums1, nums2))
