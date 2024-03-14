def select_astronaut(remaining_candidates, current_index, rhythm_parts):
    if len(remaining_candidates) == 1:
        return remaining_candidates[0]

    next_index = (current_index + rhythm_parts - 1) % len(remaining_candidates)

    remaining_candidates.pop(next_index)

    return select_astronaut(remaining_candidates, next_index, rhythm_parts)


def main():
    n = int(input())
    k = int(input())

    candidates = list(range(1, n + 1))

    print(select_astronaut(candidates, 0, k))


if __name__ == "__main__":
    main()
