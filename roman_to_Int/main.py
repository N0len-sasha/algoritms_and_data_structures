symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }


def romanToInt(s):
    sum = 0
    prev_value = 0
    for c in s:
        curr_value = symbols[c]
        if curr_value > prev_value:
            sum += curr_value - 2 * prev_value
        else:
            sum += curr_value
        prev_value = curr_value

    return sum


print(romanToInt(s='III'))

print(romanToInt(s='LVIII'))

print(romanToInt(s='MCMXCIV'))
