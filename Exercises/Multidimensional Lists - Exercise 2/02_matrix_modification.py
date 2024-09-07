matrix = [list(map(int, input().split(" "))) for i in range(int(input()))]

while True:
    commands = input()

    if commands == "END":
        break

    command, row, col, value = commands.split()

    if not (0 <= int(row) <= len(matrix)-1 and 0 <= int(col) <= len(matrix)-1):
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[int(row)][int(col)] += int(value)

    elif command == "Subtract":
        matrix[int(row)][int(col)] -= int(value)

for m_row in matrix:
    print(*m_row)
