from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments_as_stack = [int(x) for x in input().split()]

h_items = {"Patch": 30, "Bandage": 40, "MedKit": 100}
created_items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medicaments_as_stack:
    textile = textiles[0]
    medicament = medicaments_as_stack[-1]

    result = textile + medicament

    if result in h_items.values():
        key = [key for key, value in h_items.items() if value == result]
        created_items[key[0]] += 1
        textiles.popleft()
        medicaments_as_stack.pop()

    elif result > h_items["MedKit"]:
        created_items["MedKit"] += 1
        textiles.popleft()
        medicaments_as_stack.pop()
        medicaments_as_stack.append(medicaments_as_stack.pop() + result - h_items["MedKit"])

    else:
        textiles.popleft()
        medicaments_as_stack[-1] += 10

if not textiles and not medicaments_as_stack:
    print("Textiles and medicaments are both empty.")

elif not textiles:
    print("Textiles are empty.")

elif not medicaments_as_stack:
    print("Medicaments are empty.")


sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))

for item in sorted_items:
    if item[1]:
        print(f"{item[0]} - {item[1]}")

if medicaments_as_stack:
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments_as_stack[::-1])}")

if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
