def build_merged_array(nums1, nums2):
    min_1 = 0
    min_2 = 0
    new_array = []
    while (min_1 <= len(nums1) - 1 and min_2 <= len(nums2) - 1):
        if nums1[min_1] <= nums2[min_2]:
            new_array.append(nums1[min_1])
            min_1 += 1
        else:
            new_array.append(nums2[min_2])
            min_2 += 1

    if min_1 < len(nums1):
        for i in range(min_1, len(nums1)):
            new_array.append(nums1[i])
    elif min_2 < len(nums2):
        for i in range(min_2, len(nums2)):
            new_array.append(nums2[i])

    return new_array


def find_median_sorted_arrays(nums1, nums2):
    merged_arr = build_merged_array(nums1, nums2)
    print(merged_arr)

    if len(merged_arr) == 1:
        if len(nums1) == 0:
            return nums2[0]
        return nums1[0]

    index = (len(merged_arr)) // 2
    if len(merged_arr) % 2 == 0:
        return (float(merged_arr[index] + merged_arr[index - 1])) / 2
    return merged_arr[index]


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    # nums1 = [1, 2]
    # nums2 = [3, 4]
    # nums1 = [3]
    # nums2 = [-2, -1]
    print(find_median_sorted_arrays(nums1, nums2))
