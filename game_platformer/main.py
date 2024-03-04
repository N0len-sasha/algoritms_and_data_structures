def final_position(commands):
    direction = 1
    position = 0

    for command in commands:
        if command == "R":
            direction = 1
        elif command == "L":
            direction = -1
        else:
            position += direction

    return position


def change_commands(commands, commands_count):
    final_positions = set()

    for i, original_command in enumerate(commands):
        for new_command in ["F", "L", "R"]:
            if new_command != original_command:
                modified_commands = list(commands)
                modified_commands[i] = new_command
                final_positions.add(final_position(modified_commands))

    return len(final_positions)


if __name__ == '__main__':
    commands_count = int(input())
    commands = input().strip()
    print(change_commands(commands, commands_count))
