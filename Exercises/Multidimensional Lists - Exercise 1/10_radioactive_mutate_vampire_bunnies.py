def spread_bunnies(matrix, bunnies):
    new_bunnies = set()
    for bunny in bunnies:
        for direction in directions.values():
            new_row = bunny[0] + direction[0]
            new_col = bunny[1] + direction[1]
            if 0 <= new_row < int(n) and 0 <= new_col < int(m):
                if matrix[new_row][new_col] == "." or matrix[new_row][new_col] == "P":
                    new_bunnies.add((new_row, new_col))
    for bunny in new_bunnies:
        matrix[bunny[0]][bunny[1]] = "B"
    return list(new_bunnies)

n, m = input().split()


matrix = []
my_position = ()
bunny_positions = []

for row in range(int(n)):
    matrix.append(list(input()))
    for col in range(int(m)):
        if matrix[row][col] == "P":
            my_position = row, col

        elif matrix[row][col] == "B":
            bunny_positions.append((row,col))

commands = list(input())

directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

has_won = False
has_lost = False
for direction in commands:

    if has_won or has_lost:
        break

    n_row = my_position[0] + directions[direction][0]
    n_col = my_position[1] + directions[direction][1]

    if not(0 <= n_row < int(n) and 0 <= n_col < int(m)):
        has_won = True
        matrix[my_position[0]][my_position[1]] = "."
        bunny_positions.extend(spread_bunnies(matrix, bunny_positions))
        break

    if matrix[n_row][n_col] == "B":
        matrix[my_position[0]][my_position[1]] = "."
        bunny_positions.extend(spread_bunnies(matrix, bunny_positions))
        my_position = n_row, n_col
        has_lost = True
        break

    matrix[my_position[0]][my_position[1]] = "."
    matrix[n_row][n_col] = "P"
    my_position = n_row, n_col

    bunny_positions.extend(spread_bunnies(matrix, bunny_positions))

    if matrix[my_position[0]][my_position[1]] == "B":
        has_lost = True


for row in matrix:
    print("".join(row))

if has_won:
    print(f"won: {my_position[0]} {my_position[1]}")
elif has_lost:
    print(f"dead: {my_position[0]} {my_position[1]}")
