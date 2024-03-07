def two_to_one(a, b, c):
    if a % 2 + b % 2 + c % 2 in [1, 2]:
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    n = int(input())
    while n != 0:
        a, b, c = map(int, input().split())
        print(two_to_one(a, b, c))
        n -= 1
