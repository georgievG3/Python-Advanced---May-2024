from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

DOLL_MAGIC = 150
WOODEN_TRAIN_MAGIC = 250
TEDDY_BEAR_MAGIC = 300
BICYCLE_MAGIC = 400

pair_one = {"Doll", "Wooden train"}
pair_two = {"Teddy bear", "Bicycle"}

crafted_toys = {}

while materials and magic_levels:
    if materials[-1] == 0 and magic_levels[0] == 0:
        magic_levels.popleft()
        materials.pop()
        continue

    if materials[-1] == 0:
        materials.pop()
        continue
    if magic_levels[0] == 0:
        magic_levels.popleft()
        continue

    material = materials[-1]
    magic = magic_levels[0]
    magic_product = material * magic

    if magic_product == DOLL_MAGIC:
        crafted_toys["Doll"] = crafted_toys.get("Doll", 0) + 1
        materials.pop()
        magic_levels.popleft()
    elif magic_product == WOODEN_TRAIN_MAGIC:
        crafted_toys["Wooden train"] = crafted_toys.get("Wooden train", 0) + 1
        materials.pop()
        magic_levels.popleft()
    elif magic_product == TEDDY_BEAR_MAGIC:
        crafted_toys["Teddy bear"] = crafted_toys.get("Teddy bear", 0) + 1
        materials.pop()
        magic_levels.popleft()
    elif magic_product == BICYCLE_MAGIC:
        crafted_toys["Bicycle"] = crafted_toys.get("Bicycle", 0) + 1
        materials.pop()
        magic_levels.popleft()
    elif magic_product < 0:
        materials.append(materials.pop() + magic_levels.popleft())
    else:
        magic_levels.popleft()
        materials[-1] += 15

sorted_toys = sorted(crafted_toys.items())

if pair_one.issubset(crafted_toys.keys()) or pair_two.issubset(crafted_toys.keys()):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, materials[::-1]))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

# Printing the crafted toys
for toy, count in sorted_toys:
    print(f"{toy}: {count}")
