def plotter(x, y, count, commands):
    start_x = 0
    start_y = 0
    unique_segments = set()
    current_x, current_y = start_x, start_y

    for command in commands:
        match command:
            case 'R':
                next_x, next_y = current_x + 1, current_y
            case 'L':
                next_x, next_y = current_x - 1, current_y
            case 'U':
                next_x, next_y = current_x, current_y + 1
            case 'D':
                next_x, next_y = current_x, current_y - 1

        segment = ((current_x, current_y), (next_x, next_y))
        reversed_segment = ((next_x, next_y), (current_x, current_y))

        unique_segments.add(segment)
        unique_segments.add(reversed_segment)

        current_x, current_y = next_x, next_y

    return len(unique_segments) // 2


if __name__ == '__main__':
    n, m = map(int, input().split())
    c = int(input())
    s = input()
    print(plotter(n, m, c, s))
