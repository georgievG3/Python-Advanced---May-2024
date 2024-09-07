from collections import deque

milligrams_caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

MAXIMUM_CAFFEINE = 300
initial_caffeine = 0

while milligrams_caffeine and energy_drinks:

    result = milligrams_caffeine[-1] * energy_drinks[0]

    if result + initial_caffeine <= MAXIMUM_CAFFEINE:
        initial_caffeine += result
        milligrams_caffeine.pop()
        energy_drinks.popleft()

    else:
        milligrams_caffeine.pop()
        energy_drinks.append(energy_drinks.popleft())

        if initial_caffeine >= 30:
            initial_caffeine -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join(str(r) for r in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {initial_caffeine} mg caffeine.")
