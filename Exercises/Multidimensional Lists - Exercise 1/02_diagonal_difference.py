number = int(input())

matrix = [list(map(int, input().split(" "))) for i in range(number)]

primary_diagonal = [matrix[el][el] for el in range(number)]
secondary_diagonal = [matrix[el][-el - 1] for el in range(number)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
