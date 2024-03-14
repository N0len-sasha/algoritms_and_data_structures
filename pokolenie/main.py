def count_zamer(pokolenie, count, prev):
    if pokolenie <= 1:
        print(count)
        return

    a = count
    count = count + prev
    prev = a
    count_zamer(pokolenie - 1, count, prev)


if __name__ == '__main__':
    count = 1
    prev = 1
    pokolenie = int(input())
    count_zamer(pokolenie=pokolenie, count=count, prev=prev)
