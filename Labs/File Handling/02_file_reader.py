numbers_sum = 0

file = open("numbers.txt")

for line in file:
    numbers_sum += int(line)

print(numbers_sum)