n, m = input().split(",")

matrix = []
mouse_position = ()
cheese_count = 0

for row in range(int(n)):
    matrix.append(list(input()))
    for col in range(int(m)):

        if matrix[row][col] == "M":
            mouse_position = row, col

        elif matrix[row][col] == "C":
            cheese_count += 1

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()

    if command == "danger":
        if cheese_count:
            print("Mouse will come back later!")
        break

    n_row = mouse_position[0] + directions[command][0]
    n_col = mouse_position[1] + directions[command][1]

    if not(0 <= n_row < int(n) and 0 <= n_col < int(m)):
        print("No more cheese for tonight!")
        break

    if matrix[n_row][n_col] == "@":
        continue

    matrix[mouse_position[0]][mouse_position[1]] = "*"

    if matrix[n_row][n_col] == "C":
        cheese_count -= 1

        if cheese_count == 0:
            matrix[n_row][n_col] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif matrix[n_row][n_col] == "T":
        matrix[n_row][n_col] = "M"
        print("Mouse is trapped!")
        break

    matrix[n_row][n_col] = "M"
    mouse_position = n_row, n_col

for r in matrix:
    print(''.join(r))