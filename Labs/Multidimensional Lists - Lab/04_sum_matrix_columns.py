rows, columns = list(map(int, input().split(", ")))

matrix = [list(map(int, input().split())) for i in range(rows)]

for column_index in range(columns):
    columns_sum = 0
    for row_index in range(rows):
        columns_sum += matrix[row_index][column_index]

    print(columns_sum)
