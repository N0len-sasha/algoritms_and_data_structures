def determine_index(data, search_value):
    left = 0
    right = len(data)
    while left < right:
        mid = (left + right) // 2
        if int(data[mid]) == search_value:
            return mid
        if int(data[mid]) < search_value:
            left = mid + 1
        else:
            right = mid - 1
    return mid + 1


if __name__ == '__main__':
    probs = input().split(' ')
    value = int(input())
    print(determine_index(probs, value))
