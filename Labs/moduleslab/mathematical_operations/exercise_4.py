from Labs.moduleslab.mathematical_operations.core import mapper

number_one, sign, number_two = input().split()

number_one = float(number_one)
number_two = int(number_two)

print(mapper[sign](number_one, number_two))
