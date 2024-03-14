def check_nickname(nickname):
    if len(nickname) < 8:
        return 'NO'

    if not any(char.isdigit() for char in nickname):
        return 'NO'

    if not any(char.isupper() for char in nickname):
        return 'NO'

    if not any(char.islower() for char in nickname):
        return 'NO'

    return 'YES'


if __name__ == "__main__":
    nickname = input()
    print(check_nickname(nickname))
