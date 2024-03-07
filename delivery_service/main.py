# 109048615
def platforms_count(limit: int, robots: list):
    left: int = 0
    right: int = len(robots) - 1
    platforms: int = 0
    while right - left >= 1:
        if robots[right] + robots[left] <= limit:
            platforms += 1
            right -= 1
            left += 1
        else:
            platforms += 1
            right -= 1

    if right - left == 0:
        platforms += 1

    return platforms


if __name__ == '__main__':
    robots = list(map(int, input().split(' ')))
    limit = int(input())
    print(platforms_count(limit, sorted(robots)))
