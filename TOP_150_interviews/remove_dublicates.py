def removeDuplicates(nums):
        unique_nums = list(set(nums))
        unique_nums.sort()
        unique_count = len(unique_nums)
        for i in range(len(nums)):
            if i >= unique_count:
                nums[i] = '_'
            else:
                nums[i] = unique_nums[i]
        return unique_count


if __name__ == '__main__':
    nums = [-1,0,0,0,0,3,3]
    print(removeDuplicates(nums), nums)
