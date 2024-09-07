matrix = []

my_position = (0, 0)
targets = 0
targets_hit = []

moves = {"down": (1, 0), "up": (-1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == "A":
            my_position = (row, col)

        elif matrix[row][col] == "x":
            targets += 1

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()

    if command[0] == "shoot":
        direction = command[1]
        bullet_position = [my_position[0] + moves[direction][0], my_position[1] + moves[direction][1]]

        while 0 <= bullet_position[0] < 5 and 0 <= bullet_position[1] < 5:
            if matrix[bullet_position[0]][bullet_position[1]] == "x":
                matrix[bullet_position[0]][bullet_position[1]] = "."
                targets -= 1
                targets_hit.append([bullet_position[0], bullet_position[1]])
                break

            bullet_position[0] += moves[direction][0]
            bullet_position[1] += moves[direction][1]

        if targets == 0:
            print(f"Training completed! All {len(targets_hit)} targets hit.")
            break

    elif command[0] == "move":
        direction = command[1]
        steps = int(command[2])

        next_position = (my_position[0] + moves[direction][0] * steps, my_position[1] + moves[direction][1] * steps)

        if 0 <= next_position[0] < 5 and 0 <= next_position[1] < 5 and matrix[next_position[0]][next_position[1]] == ".":
            matrix[next_position[0]][next_position[1]] = "A"
            matrix[my_position[0]][my_position[1]] = "."
            my_position = next_position


if targets > 0:
    print(f"Training not completed! {targets} targets left.")

print(*targets_hit, sep="\n")