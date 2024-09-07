number = int(input())

QUOTA = 20

matrix = []
my_position = ()
quantity = 0

for row in range(number):
    matrix.append(list(input()))
    for col in range(number):
        if matrix[row][col] == "S":
            my_position = row, col

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()

    if command == "collect the nets":
        break

    matrix[my_position[0]][my_position[1]] = "-"
    n_row = my_position[0] + directions[command][0]
    n_col = my_position[1] + directions[command][1]

    if not(0 <= n_row < number and 0 <= n_col < number):
        if command == "down":
            n_row = 0

        elif command == "up":
            n_row = number - 1

        elif command == "left":
            n_col = number - 1

        elif command == "right":
            n_col = 0


    if matrix[n_row][n_col] == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{n_row},{n_col}]")
        quantity = 0
        exit()

    elif matrix[n_row][n_col] != "-":
        quantity += int(matrix[n_row][n_col])

    matrix[n_row][n_col] = "S"
    my_position = n_row, n_col

if quantity >= QUOTA:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {QUOTA - quantity} tons of fish more.")

if quantity > 0:
    print(f"Amount of fish caught: {quantity} tons.")

for r in matrix:
    print("".join(r))
