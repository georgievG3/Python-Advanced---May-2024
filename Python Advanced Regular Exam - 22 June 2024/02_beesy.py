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
            bee_position = row, col

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

extra_life = True
while True:
    command = input()
    initial_energy -= 1

    n_row = bee_position[0] + directions[command][0]
    n_col = bee_position[1] + directions[command][1]

    if n_row > number:
        n_row = 0
    if n_row < 0:
        n_row = number - 1
    if n_col > number:
        n_col = 0
    if n_col < 0:
        n_col = number - 1

    if matrix[n_row][n_col] == "H":
        if initial_energy <= 0 and nectar_collected < MINIMUM_TO_COLLECT:
            print("This is the end! Beesy ran out of energy.")
            print("Beesy did not manage to collect enough nectar.")
            break

        if nectar_collected >= MINIMUM_TO_COLLECT:
            matrix[bee_position[0]][bee_position[1]] = "-"
            matrix[n_row][n_col] = "B"
            print(f"Great job, Beesy! The hive is full. Energy left: {initial_energy}")
            break

    if initial_energy <= 0 and nectar_collected < MINIMUM_TO_COLLECT:
        print("This is the end! Beesy ran out of energy.")
        break

    elif initial_energy <= 0 and nectar_collected >= MINIMUM_TO_COLLECT:

        if extra_life:
            initial_energy += nectar_collected - MINIMUM_TO_COLLECT
            nectar_collected = 30
            extra_life = False
            matrix[bee_position[0]][bee_position[1]] = "-"
            matrix[n_row][n_col] = "B"

        if initial_energy <= 0:
            print("This is the end! Beesy ran out of energy.")
            break

    elif matrix[n_row][n_col] != "-":
        nectar_collected += int(matrix[n_row][n_col])
        matrix[bee_position[0]][bee_position[1]] = "-"
        matrix[n_row][n_col] = "-"
        bee_position = n_row, n_col

for r in matrix:
    print("".join(r))
