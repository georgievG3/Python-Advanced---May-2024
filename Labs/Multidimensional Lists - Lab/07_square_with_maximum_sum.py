rows, columns = list(map(int, input().split(", ")))

matrix = [[int(el) for el in input().split(", ")] for i in range(rows)]

max_sum = float('-inf')

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]

        current_sum = sum((current_element, next_element, element_below, element_diagonal))

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_element, next_element], [element_below, element_diagonal]]

print(*sub_matrix[0], sep=" ")
print(*sub_matrix[1], sep=" ")

print(max_sum)
