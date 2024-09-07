# numbers = tuple(float(num) for num in input().split())
#
# occ = []
#
# for n in numbers:
#     if n not in occ:
#         occ.append(n)
#
# for number in occ:
#     print(f"{number:.1f} - {numbers.count(number)} times")

numbers = tuple(float(num) for num in input().split())

occ = {}

for n in numbers:
    occ[n] = numbers.count(n)

for key, value in occ.items():
    print(f"{key:.1f} - {value} times")