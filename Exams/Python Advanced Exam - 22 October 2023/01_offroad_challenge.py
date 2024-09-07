from collections import deque

initial_fuel = list(map(int, input().split()))
additional_consumption = deque(list(map(int, input().split())))
fuel_needed = deque(list(map(int, input().split())))
altitudes = deque([1, 2, 3, 4])
reached_altitudes = []

while fuel_needed:

    if initial_fuel[-1] - additional_consumption[0] >= fuel_needed[0]:
        initial_fuel.pop()
        additional_consumption.popleft()
        fuel_needed.popleft()
        print(f"John has reached: Altitude {altitudes[0]}")
        reached_altitudes.append(f"Altitude {altitudes.popleft()}")

    else:
        print(f"John did not reach: Altitude {altitudes[0]}")
        break

if not fuel_needed:
    print("John has reached all the altitudes and managed to reach the top!")

elif len(altitudes) == 4:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")

else:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached_altitudes)}")
