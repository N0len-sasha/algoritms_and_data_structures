def twoSum(nums, target):
    indexies = []

    for j in range(len(nums)):
        for i in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                indexies.append(j)
                indexies.append(i)
                return indexies


print(twoSum(nums=[3, 2, 4], target=6))

print(twoSum(nums=[2, 7, 11, 15], target=9))

print(twoSum(nums=[3, 3], target=6))
