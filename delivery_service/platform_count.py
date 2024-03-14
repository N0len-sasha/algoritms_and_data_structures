def platforms_count(limit: int, weights: list) -> int:
    sorted_weights = sorted(weights)
    min_weight_index: int = 0
    max_weight_index: int = len(sorted_weights) - 1
    platforms: int = 0

    while min_weight_index <= max_weight_index:
        if sorted_weights[min_weight_index] + sorted_weights[max_weight_index] <= limit:
            min_weight_index += 1
        max_weight_index -= 1
        platforms += 1

    return platforms


if __name__ == '__main__':
    weights = list(map(int, input().split(' ')))
    limit = int(input())
    print(platforms_count(limit=limit, weights=weights))
