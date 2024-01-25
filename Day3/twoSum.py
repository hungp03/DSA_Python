def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def twoSumV2(nums, target):
    numToIndex = {}
    for i, num in enumerate(nums):
        if target - num in numToIndex:
            return [numToIndex[target - num], i]
        numToIndex[num] = i


nums = [2, 7, 11, 15]
target = 9
print(twoSumV2(nums, target))
