number = int(input())
car_number = input()

my_position = (0, 0)
tunnel_one = ()
tunnel_two = ()
distance = 0
matrix = []

for row in range(number):
    matrix.append(input().split())
    for col in range(number):

        if matrix[row][col] == "T":

            if not tunnel_one:
                tunnel_one = row, col
            else:
                tunnel_two = row, col

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()

    if command == "End":
        print(f"Racing car {car_number} DNF.") #!
        break

    n_row = my_position[0] + directions[command][0]
    n_col = my_position[1] + directions[command][1]

    if matrix[n_row][n_col] == "F":
        print(f"Racing car {car_number} finished the stage!")
        distance += 10
        my_position = n_row, n_col
        break

    if matrix[n_row][n_col] == "T":

        if (n_row, n_col) == tunnel_one:
            my_position = tunnel_two
            distance += 30
            matrix[tunnel_one[0]][tunnel_one[1]] = "."
            matrix[tunnel_two[0]][tunnel_two[1]] = "."
            continue

    distance += 10
    my_position = n_row, n_col

matrix[my_position[0]][my_position[1]] = "C"

print(f"Distance covered {distance} km.")
for r in matrix:
    print("".join(r))
