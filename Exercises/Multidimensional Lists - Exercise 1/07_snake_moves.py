rows, columns = list(map(int, input().split()))
snake_string = list(input())

matrix = []

for row in range(rows):
    data = []

    for column in range(columns):
        data.append(snake_string[0])
        popped_item = snake_string.pop(0)
        snake_string.append(popped_item)

    if row % 2 == 0:
        matrix.append(data)

    else:
        matrix.append(data[::-1])

[print(''.join(row)) for row in matrix]
