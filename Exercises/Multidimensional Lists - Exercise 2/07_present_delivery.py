number_of_presents = int(input())
number = int(input())

matrix = []
nice_kids = 0
santa_position = ()
count_nice_kids = 0

for row in range(number):
    matrix.append(input().split())
    for col in range(number):
        if matrix[row][col] == "S":
            santa_position = row, col
        elif matrix[row][col] == "V":
            nice_kids += 1

moves = {"down": (1, 0), "up": (-1, 0), "left": (0, -1), "right": (0, 1)}

command = input()
while command != "Christmas morning":
    matrix[santa_position[0]][santa_position[1]] = "-"
    n_row = santa_position[0] + moves[command][0]
    n_col = santa_position[1] + moves[command][1]

    if matrix[n_row][n_col] == "V":
        number_of_presents -= 1
        nice_kids -= 1
        count_nice_kids += 1

    elif matrix[n_row][n_col] == "C":
        for key, value in moves.items():
            if number_of_presents > 0:
                if matrix[n_row + int(moves[key][0])][n_col + int(moves[key][1])] == "V":
                    nice_kids -= 1
                    count_nice_kids += 1
                    number_of_presents -= 1
                if matrix[n_row + int(moves[key][0])][n_col + int(moves[key][1])] == "X":
                    number_of_presents -= 1
                matrix[n_row + int(moves[key][0])][n_col + int(moves[key][1])] = "-"

            else:
                matrix[n_row + int(moves[key][0])][n_col + int(moves[key][1])] = "-"
                break

    matrix[n_row][n_col] = "S"
    santa_position = n_row, n_col

    if number_of_presents <= 0:
        break

    command = input()

if not number_of_presents and nice_kids:
    print("Santa ran out of presents!")

for r in matrix:
    print(" ".join(r))

if not nice_kids:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
