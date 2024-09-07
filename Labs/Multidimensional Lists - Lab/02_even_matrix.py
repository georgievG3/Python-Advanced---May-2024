rows = int(input())

matrix = [[int(el) for el in input().split(", ") if int(el) % 2 == 0] for i in range(rows)]

print(matrix)

#Solution 2
# rows = int(input())
#
# matrix = []
# even = []
#
# for _ in range(rows):
#     matrix.append(list(map(int, input().split(", "))))
#
#
# for row in matrix:
#     even.append([(el) for el in row if el % 2 == 0])
#
# print(even)


