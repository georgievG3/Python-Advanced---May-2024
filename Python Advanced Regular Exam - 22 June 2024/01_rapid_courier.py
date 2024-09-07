from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque(int(x) for x in input().split())

total_weight_delivered = 0

while packages and couriers:

    last_package = packages[-1]
    first_courier = couriers[0]

    if first_courier == last_package:
        total_weight_delivered += packages.pop()
        couriers.popleft()

    elif first_courier > last_package:
        couriers[0] -= last_package * 2

        if couriers[0] > 0:
            couriers.append(couriers.popleft())

        else:
            couriers.popleft()

        total_weight_delivered += packages.pop()

    else:
        packages[-1] -= first_courier
        couriers.popleft()
        total_weight_delivered += first_courier

print(f"Total weight: {total_weight_delivered} kg")

if packages:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(str(x) for x in packages)}")
elif couriers:
    print(f"Couriers are still on duty: {', '.join(str(x) for x in couriers)} but there are no more packages to deliver.")
else:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
