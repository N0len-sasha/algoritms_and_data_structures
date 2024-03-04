def valid_mountain_array(values):
    values = [int(val) for val in values]

    if len(values) < 3:
        return False

    peak_index = values.index(max(values))
    if peak_index == 0 or peak_index == len(values) - 1:
        return False

    for i in range(1, peak_index):
        if values[i] <= values[i - 1]:
            return False

    for i in range(peak_index + 1, len(values)):
        if values[i] >= values[i - 1]:
            return False

    return True


if __name__ == '__main__':
    values = input().split(' ')
    print(valid_mountain_array(values=values))
