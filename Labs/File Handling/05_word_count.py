import re

with open("words.txt") as file:
    words = file.read()

words_list = words.split()

with open("input.txt") as file:
    text = file.read()

words_dict = {}

for word in words_list:
    pattern = rf"\b{word}\b"

    matches = re.findall(pattern, text, re.IGNORECASE)

    words_dict[word] = len(matches)

sorted_dict = sorted(words_dict.items(), key=lambda kvp: -kvp[1])

with open("output.txt", "w") as file:
    for k, v in sorted_dict:
        file.write(f"{k} - {v}\n")
