rows = int(input())

matrix = [list(map(int, input().split())) for i in range(rows)]
diagonal_sum = 0

for row_index in range(rows):
    for col_index in range(rows):
        if row_index == col_index:
            diagonal_sum += matrix[row_index][col_index]

print(diagonal_sum)

