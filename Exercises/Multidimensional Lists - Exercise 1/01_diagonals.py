number = int(input())

matrix = [list(map(int, input().split(", "))) for i in range(number)]

primary_diagonal = [matrix[el][el] for el in range(number)]
secondary_diagonal = [matrix[el][-el - 1] for el in range(number)]

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")

