reservation_number = int(input())

reservations = set()

for _ in range(reservation_number):
    reservation_code = input()

    reservations.add(reservation_code)

while True:
    command = input()

    if command == "END":
        break

    if command in reservations:
        reservations.remove(command)

print(len(reservations))
print(*sorted(reservations), sep="\n")