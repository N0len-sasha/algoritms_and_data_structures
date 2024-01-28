def determine_index(data, search_value):
    left = 0
    right = len(data)
    while left < right:
        mid = (left + right) // 2
        if data[mid] == search_value:
            return mid
        if data[mid] < search_value:
            left = mid + 1
        else:
            right = mid - 1
    return mid + 1


mas = [1, 3, 5, 6]
value = 5
print(determine_index(mas, value))

mas = [1, 5, 10, 11]
value = 2
print(determine_index(mas, value))

mas = [3, 7, 10, 20, 23]
value = 25
print(determine_index(mas, value))
