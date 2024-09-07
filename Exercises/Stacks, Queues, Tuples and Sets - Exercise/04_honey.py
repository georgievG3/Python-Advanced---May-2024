from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0
operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y if y!= 0 else 0,
    '*': lambda x, y: x * y
}

while bees and nectar:

    first_bee = bees[0]
    last_nectar = nectar[-1]

    if first_bee > last_nectar:
        nectar.pop()

    else:

        total_honey += abs(operators[symbols[0]](bees[0], nectar[-1]))
        nectar.pop()
        bees.popleft()
        symbols.popleft()

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
