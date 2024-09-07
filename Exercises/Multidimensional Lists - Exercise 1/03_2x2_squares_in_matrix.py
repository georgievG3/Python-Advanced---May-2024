rows, columns = list(map(int, input().split()))

matrix = [[el for el in input().split()] for _ in range(rows)]

identical_chars_count = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        main_element = matrix[row][column]
        right_element = matrix[row][column + 1]
        bottom_element = matrix[row + 1][column]
        bottom_right_element = matrix[row + 1][column + 1]

        if main_element == right_element == bottom_element == bottom_right_element:
            identical_chars_count += 1

print(identical_chars_count)
