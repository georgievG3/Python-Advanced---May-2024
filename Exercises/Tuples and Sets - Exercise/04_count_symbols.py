# text = tuple(input())
#
# characters = []
#
# for char in sorted(text):
#     occ = text.count(char)
#
#     if char not in characters:
#         print(f"{char}: {occ} time/s")
#     characters.append(char)

text = input()

text_set = set(text)

for char in sorted(text_set):
    occ = text.count(char)
    print(f"{char}: {occ} time/s")
