def int_to_Roman(x: int):
    roman = ''
    before_romans = {
        5: 'IV',
        10: 'IX',
        50: 'XL',
        100: 'XC',
        500: 'CD',
        1000: 'CM'
    }
    index = 1
    while x != 0:
        value = x % (10 ** index)
        if value in [4, 9, 40, 90, 400, 900]:
            roman = before_romans[value + (10 ** (index - 1))] + roman
        elif value in before_romans:
            roman = before_romans[value][1:] + roman
        elif value > 5 * (10 ** (index - 1)):
            roman = before_romans[5 * (10 ** (index - 1))][1:] + before_romans[5 * (10 ** (index - 1))][:1] * ((value - 5 * (10 ** (index - 1))) // (10 ** (index - 1))) + roman
        else:
            if 5 * (10 ** (index - 1)) != 5000:
                roman = before_romans[5 * (10 ** (index - 1))][:1] * (value // (10 ** (index - 1))) + roman
            else:
                roman = 'M' * (value // (10 ** (index - 1))) + roman
        x = x - x % (10 ** index)
        index += 1
    return roman


if __name__ == '__main__':
    chis = int(input())
    print(int_to_Roman(chis))
