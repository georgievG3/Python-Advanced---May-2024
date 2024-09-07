number = int(input())

matrix = []
alice_position = (0, 0)
total_bags = 0

for row in range(number):
    matrix.append(input().split())
    for col in range(number):
        if matrix[row][col] == "A":
            alice_position = (row, col)

moves = {"down": (1, 0), "up": (-1, 0), "left": (0, -1), "right": (0, 1)}

collected_ten = False
while True:
    command = input()

    matrix[alice_position[0]][alice_position[1]] = "*"
    next_position = (alice_position[0] + moves[command][0], alice_position[1] + moves[command][1])

    if not (0 <= next_position[0] < number and 0 <= next_position[1] < number):
        break

    if matrix[next_position[0]][next_position[1]] == "R":
        matrix[next_position[0]][next_position[1]] = "*"
        break

    if matrix[next_position[0]][next_position[1]].isdigit():
        total_bags += int(matrix[next_position[0]][next_position[1]])
        if total_bags >= 10:
            collected_ten = True

    matrix[next_position[0]][next_position[1]] = "*"
    alice_position = next_position

    if collected_ten:
        break

if collected_ten:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for r in matrix:
    print(" ".join(r))
