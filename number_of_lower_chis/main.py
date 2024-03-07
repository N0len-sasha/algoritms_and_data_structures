# import time

def find_lower_nums(nums):
    nums_count = []
    for num in nums:
        index = 0
        for num_2 in nums:
            if num > num_2:
                index += 1
        nums_count.append(index)
    return ' '.join(map(str, nums_count))


if __name__ == '__main__':
    nums = list(map(int, input().split(' ')))
    print(find_lower_nums(nums))
