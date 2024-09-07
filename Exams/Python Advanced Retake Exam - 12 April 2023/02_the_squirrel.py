number = int(input())
commands = input().split(", ")

hazelnuts_count = 0
matrix = []
squirrel_position = ()

for row in range(number):
    matrix.append(list(input()))
    for col in range(number):
        if matrix[row][col] == "s":
            squirrel_position = row, col

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

did_lose = False
for direction in commands:

    n_row = squirrel_position[0] + directions[direction][0]
    n_col = squirrel_position[1] + directions[direction][1]

    if not(0 <= n_row < number and 0 <= n_col < number):
        print(f"The squirrel is out of the field.")
        did_lose = True
        break

    if matrix[n_row][n_col] == "h":
        hazelnuts_count += 1

        if hazelnuts_count == 3:
            print(f"Good job! You have collected all hazelnuts!")
            matrix[n_row][n_col] = "*"
            break

    if matrix[n_row][n_col] == "t":
        print(f"Unfortunately, the squirrel stepped on a trap...")
        did_lose = True
        break

    matrix[squirrel_position[0]][squirrel_position[1]] = "*"
    matrix[n_row][n_col] = "s"
    squirrel_position = n_row, n_col

if hazelnuts_count != 3 and not did_lose:
    print(f"There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts_count}")
