rows = int(input())

flattened = []

for i in range(rows):
    row_data = [int(el) for el in input().split(", ")]
    flattened.extend(row_data)
print(flattened)

#Solution 1
# rows = int(input())
#
# matrix = [list(map(int, input().split(", "))) for i in range(rows)]
#
# flattened = [num for row in matrix for num in row]
#
# print(flattened)