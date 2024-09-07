number = int(input())
commands = input().split()

matrix = [input().split() for _ in range(number)]

row_position, column_position = list([(row, col) for row in range(number) for col in range(number) if matrix[row][col] == 's'][0])
coal_count = sum([1 for row in range(number) for col in range(number) if matrix[row][col] == 'c'])

found_coal = 0
found_all_coal = False
game_over = False
for command in commands:

    if command == "up":
        if row_position > 0:
            row_position -= 1

    elif command == "right":
        if column_position < number - 1:
            column_position += 1

    elif command == "left":
        if column_position > 0:
            column_position -= 1

    elif command == "down":
        if row_position < number - 1:
            row_position += 1

    if matrix[row_position][column_position] == "e":
        game_over = True
        break

    elif matrix[row_position][column_position] == "c":
        matrix[row_position][column_position] = "*"
        found_coal += 1

        if found_coal == coal_count:
            found_all_coal = True
            break

if game_over:
    print(f"Game over! ({row_position}, {column_position})")

elif found_all_coal:
    print(f"You collected all coal! ({row_position}, {column_position})")

else:
    print(f"{coal_count - found_coal} pieces of coal left. ({row_position}, {column_position})")
