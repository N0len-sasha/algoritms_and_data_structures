def is_valid(s):
    values = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    stack = []
    for char in s:
        if char in values:
            stack.append(char)
        elif char in values.values():
            if not stack or values[stack.pop()] != char:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    s = list(input())
    print(is_valid(s=s))



# s_false = '( { ] )'.split(' ')
# s_true_1 = '( { [ ] } )'.split(' ')
# s_true_2 = '( { [ ] } ) ( [ ] )'.split(' ')
# print(is_valid(s_false))
# print(is_valid(s_true_1))
# print(is_valid(s_true_2))
