def reverse_number(number):
    if not (number >= -2**31 and number <= 2**31 - 1):
        return 0

    number_abs = abs(number)
    s = ''

    while number_abs // 10 != 0:
        s += str((number_abs % 10))
        number_abs = number_abs // 10

    s = s + str(number_abs % 10)

    if number < 0:
        return int(s) * -1
    return int(s)


if __name__ == '__main__':
    x = int(input())
    print(reverse_number(x))
