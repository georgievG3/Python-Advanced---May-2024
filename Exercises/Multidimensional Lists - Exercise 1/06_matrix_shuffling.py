rows, columns = list(map(int, input().split()))

matrix = [input().split() for i in range(rows)]

while True:
    data_info = input()

    if data_info == "END":
        break

    data = data_info.split()

    if data[0] != "swap" or len(data) > 5 or not 0 <= int(data[1]) < rows or not 0 <= int(data[2]) < columns or not 0 <= int(data[3]) < rows or not 0 <= int(data[4]) < columns:
        print("Invalid input!")

    else:
        row1, col1, row2, col2 = list(map(int, data[1:]))

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
