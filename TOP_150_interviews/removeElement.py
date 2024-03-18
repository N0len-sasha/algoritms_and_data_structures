def removeElement(nums, val):
    index = 0
    while val in nums:
        nums.remove(val)
        index += 1
    for i in range(len(nums), len(nums) + index):
        nums.append('_')
    return len(nums) - index


if __name__ == '__main__':
    nums = [3, 2, 2, 3, 3]
    val = 3
    print(removeElement(nums, val))
    print(nums)
