number = int(input())

matrix = []
initial_energy = 15
nectar_collected = 0
MINIMUM_TO_COLLECT = 30
bee_position = ()

for row in range(number):
    matrix.append(list(input()))
    for col in range(number):
        if matrix[row][col] == "B":
            bee_position = (row, col)

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

extra_life = True
reached_the_hive = False

while initial_energy and not reached_the_hive:
    command = input()

    n_row = bee_position[0] + directions[command][0]
    n_col = bee_position[1] + directions[command][1]

    if n_row >= number:
        n_row = 0
    elif n_row < 0:
        n_row = number - 1
    if n_col >= number:
        n_col = 0
    elif n_col < 0:
        n_col = number - 1

    initial_energy -= 1

    if matrix[n_row][n_col] == "H":
        reached_the_hive = True
        matrix[bee_position[0]][bee_position[1]] = "-"
        matrix[n_row][n_col] = "B"
        break

    if matrix[n_row][n_col] != "-":
        nectar_collected += int(matrix[n_row][n_col])
        matrix[n_row][n_col] = "-"

    matrix[bee_position[0]][bee_position[1]] = "-"
    matrix[n_row][n_col] = "B"
    bee_position = (n_row, n_col)

    if initial_energy <= 0:
        if nectar_collected >= MINIMUM_TO_COLLECT and extra_life:
            restored_energy = nectar_collected - MINIMUM_TO_COLLECT
            initial_energy += restored_energy
            nectar_collected = 30
            extra_life = False

        if initial_energy <= 0:
            break

if reached_the_hive and nectar_collected >= MINIMUM_TO_COLLECT:
    print(f"Great job, Beesy! The hive is full. Energy left: {initial_energy}")
elif reached_the_hive and nectar_collected < MINIMUM_TO_COLLECT:
    print("Beesy did not manage to collect enough nectar.")
else:
    print("This is the end! Beesy ran out of energy.")

for r in matrix:
    print("".join(r))
