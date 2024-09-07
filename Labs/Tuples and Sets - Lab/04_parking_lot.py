car_count = int(input())

cars = set()

for _ in range(car_count):
    command, car_number = input().split(", ")

    if command == "IN":
        cars.add(car_number)

    elif command == "OUT":
        if car_number in cars:
            cars.remove(car_number)

if cars:
    print(*cars, sep="\n")

else:
    print("Parking Lot is Empty")