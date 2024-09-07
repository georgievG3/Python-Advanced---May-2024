rows, columns = list(map(int, input().split()))

matrix = []

for i in range(rows):
    row_data = []
    for j in range(columns):
        row_data.append(f"{chr(97 + i)}{chr(97 + j + i)}{chr(97 + i)}")

    matrix.append(row_data)

[print(*row) for row in matrix]
