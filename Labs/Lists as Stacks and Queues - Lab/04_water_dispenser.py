from collections import deque

liters_of_water = int(input())
queue = deque([])

while True:
    name = input()

    if name == "Start":
        break

    queue.append(name)

while True:
    command = input()

    if command == "End":
        break

    if command.isdigit():
        litres = int(command)

        if liters_of_water >= litres:
            liters_of_water -= litres
            print(f"{queue.popleft()} got water" )

        else:
            print(f"{queue.popleft()} must wait")

    else:
        _, refilled_liters = command.split()

        liters_of_water += int(refilled_liters)

print(f"{liters_of_water} liters left")
