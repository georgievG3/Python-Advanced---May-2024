num1, num2 = list(map(int, input().split()))

first_set = set()
second_set = set()

for n1 in range(num1):
    first_set.add(int(input()))

for n2 in range(num2):
    second_set.add(int(input()))

unique_elements = first_set.intersection(second_set)

print(*unique_elements, sep="\n")
c