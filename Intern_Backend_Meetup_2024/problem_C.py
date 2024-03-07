def emotional(events):
    max_emotion = -1
    min_length = len(events) + 1
    left = 0
    start, end = 0, 0

    if len(set(events)) == 1:
        return events[0]

    for right in range(1, len(events)):
        emotion = abs(ord(events[right]) - ord(events[left]))
        if emotion > max_emotion:
            min_length = right - left
            max_emotion = emotion
            start = left
            end = right
        elif emotion == max_emotion:
            if right - left < min_length:
                min_length = right - left
                start = left
                end = right
            left += 1
        else:
            left += 1

    return events[start:end+1]


if __name__ == '__main__':
    s = input().strip()
    print(emotional(s))
