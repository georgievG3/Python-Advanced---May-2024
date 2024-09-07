input_string = input()

sublists = input_string.split('|')

matrix = []

for sublist in sublists:
    numbers = sublist.strip().split()
    if numbers:
        matrix.append(numbers)

result = ""

for sublist in matrix[::-1]:
    result += ' '.join(sublist) + ' '

print(result.strip())

# matrix = []
#
# text = input().split("|")
#
# for i in range(len(text)):
#     matrix.append(text[i].strip().split())
#
# result = ""
# for item in (matrix[::-1]):
#     result += ' '.join(item) + ' '
#
# print(result.strip())
#
