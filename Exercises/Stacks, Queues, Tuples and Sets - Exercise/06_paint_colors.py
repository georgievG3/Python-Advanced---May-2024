from collections import deque

main_colors = {"red", "yellow", "blue"}
secondary_colors = {
        "orange": {"red", "yellow"},
        "purple": {"red", "blue"},
        "green": {"yellow", "blue"}
    }

all_colors = main_colors.union(secondary_colors)

substrings = deque(input().split())
found_colors = []

while substrings:

    if len(substrings) == 1:
        first = substrings.pop()
        last = ""

    else:
        first = substrings.popleft()
        last = substrings.pop()

    if first + last in all_colors:
        found_colors.append(first + last)

    elif last + first in all_colors:
        found_colors.append(last + first)

    else:
        first = first[:-1]
        last = last[:-1]

        if first:
            substrings.insert(len(substrings) // 2, first)
        if last:
            substrings.insert((len(substrings) + 1) // 2, last)

final_colors = []

for color in found_colors:
    if color in main_colors:
        final_colors.append(color)

    elif color in secondary_colors:
        if secondary_colors[color].issubset(set(found_colors)):
            final_colors.append(color)

print(final_colors)
