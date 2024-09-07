number = int(input())

matrix = []
bunny_position = [0, 0]

for row in range(number):
    matrix.append(input().split())
    for col in range(number):
        if matrix[row][col] == "B":
            bunny_position = [row, col]

max_sum = 0
max_cords = []
max_direction = ""

moves = {"down": (1, 0), "up": (-1, 0), "left": (0, -1), "right": (0, 1)}

for direction, move in moves.items():
    current_position = bunny_position
    current_sum = 0
    current_cords = []
    current_direction = ""

    while True:
        next_position = [current_position[0] + move[0], current_position[1] + move[1]]

        if not(0 <= next_position[0] < number and 0 <= next_position[1] < number):
            break

        if matrix[next_position[0]][next_position[1]] == "X":
            break

        current_sum += int(matrix[next_position[0]][next_position[1]])
        current_position = next_position
        current_cords.append(current_position)
        current_direction = direction

    if current_sum >= max_sum:
        max_sum = current_sum
        max_cords = current_cords
        max_direction = current_direction

print(max_direction)
print(*max_cords, sep="\n")
print(max_sum)
