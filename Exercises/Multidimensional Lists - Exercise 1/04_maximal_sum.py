rows, columns = list(map(int, input().split()))

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

max_number = float('-inf')
max_row = 0
max_col = 0

for row in range(rows - 2):
    for column in range(columns - 2):
        current_sum = 0

        for i in range(row, row + 3):
            for j in range(column, column + 3):
                current_sum += matrix[i][j]

        if current_sum > max_number:
            max_number = current_sum
            max_row = row
            max_col = column

print(f"Sum = {max_number}")

max_submatrix = [matrix[r][max_col:max_col + 3] for r in range(max_row, max_row + 3)]
[print(*row) for row in max_submatrix]
