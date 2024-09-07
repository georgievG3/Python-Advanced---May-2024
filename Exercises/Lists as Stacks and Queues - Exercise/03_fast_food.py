from collections import deque

quantity_of_food = int(input())
orders_queue = deque(input().split())

print(max(int(x) for x in orders_queue))

while orders_queue:
    first_order = int(orders_queue[0])

    if first_order <= quantity_of_food:
        quantity_of_food -= first_order
        orders_queue.popleft()

    else:
        break

if orders_queue:
    print("Orders left: ", *orders_queue)

else:
    print("Orders complete")