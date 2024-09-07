# number = int(input())
#
# unique_elements = set()
#
# for el in range(number):
#     chemical_compound = input().split()
#
#     for element in chemical_compound:
#         unique_elements.add(element)
#
# print(*unique_elements, sep="\n")

number = int(input())

unique_elements = set()

for el in range(number):
    unique_elements.update(element for element in input().split())

print(*unique_elements, sep="\n")
