#SOLUTION 1
# rows, columns = list(map(int, input().split(", ")))
#
# matrix = []
# numbers_sum = 0
#
# for i in range(rows):
#     rows_count = []
#     column = list(map(int, input().split(", ")))
#
#     for j in range(columns):
#         rows_count.append(column[j])
#
#     numbers_sum += sum(rows_count)
#     matrix.append(rows_count)
#
# print(numbers_sum)
# print(matrix)

#SOLUTION 2
# rows, columns = list(map(int, input().split(", ")))

# matrix = []
# numbers_sum = 0
#
# for i in range(rows):
#     matrix.append(list(map(int, input().split(", "))))
#     numbers_sum += sum(matrix[i])
#
# print(numbers_sum)
# print(matrix)

#almost solution 3
# rows, columns = list(map(int, input().split(", ")))
#
# matrix = [list(map(int, input().split(", "))) for i in range(rows)]
#
# print(matrix)