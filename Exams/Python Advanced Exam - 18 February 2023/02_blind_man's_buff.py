n, m = input().split()

PLAYERS_COUNT = 3

matrix = []
my_position = ()
moves_made = 0
players_touched = 0

for row in range(int(n)):
    matrix.append(input().split())
    for col in range(int(m)):
        if matrix[row][col] == "B":
            my_position = row, col

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()

    if command == "Finish":
        break

    n_row = my_position[0] + directions[command][0]
    n_col = my_position[1] + directions[command][1]

    if not(0 <= n_row < int(n) and 0 <= n_col < int(m)) or matrix[n_row][n_col] == "O":
        continue

    moves_made += 1

    if matrix[n_row][n_col] == "P":
        players_touched += 1

        if players_touched == PLAYERS_COUNT:
            break

    matrix[my_position[0]][my_position[1]] = "-"
    matrix[n_row][n_col] = "B"
    my_position = n_row, n_col

print("Game over!")
print(f"Touched opponents: {players_touched} Moves made: {moves_made}")
