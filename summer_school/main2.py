def check_string(correct, input_str):
    final_str = ''
    index = 0

    for symbol in input_str:
        if symbol[0] == '<':
            if symbol == '<delete>':
                if index < len(final_str):
                    final_str = final_str[:index] + final_str[index+1:]
            elif symbol == '<bspace>':
                if index > 0:
                    final_str = final_str[:index-1] + final_str[index:]
                    index -= 1
            elif symbol == '<left>':
                index = max(0, index - 1)
            elif symbol == '<right>':
                index = min(len(final_str), index + 1)
        else:
            final_str = final_str[:index] + symbol + final_str[index:]
            index += len(symbol)

    final_str = [symbol for symbol in final_str]
    correct = [symbol for symbol in correct]
    if final_str == correct[:len(correct) - 1]:
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    s = input()
    s1 = input()
    s1 = s1.replace('>', '> ').replace('<', ' <').split()
    print(check_string(s, s1))
