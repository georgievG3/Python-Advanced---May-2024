rows = int(input())

matrix = [[el for el in input()] for i in range(rows)]

symbol = input()

position = None
is_found = False
for row_index in range(rows):
    if position:
        break
    for column_index in range(rows):
        element = matrix[row_index][column_index]

        if element == symbol:
            is_found = True
            position = (row_index, column_index)
            break

if is_found:
    print(position)

else:
    print(f"{symbol} does not occur in the matrix")
