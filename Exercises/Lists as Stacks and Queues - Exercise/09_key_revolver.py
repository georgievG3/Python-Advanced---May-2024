from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets_stack = list(map(int, input().split()))
locks_queue = deque(list(map(int, input().split())))
intelligence_value = int(input())

bullets_fired = 0
current_barrel = barrel_size

while locks_queue and bullets_stack:

    if bullets_stack[-1] <= locks_queue[0]:
        print("Bang!")
        locks_queue.popleft()
    else:
        print("Ping!")

    bullets_stack.pop()
    current_barrel -= 1
    bullets_fired += 1

    if current_barrel == 0 and bullets_stack:
        print("Reloading!")
        current_barrel = barrel_size

if locks_queue:
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")
else:
    money_earned = intelligence_value - bullets_fired * bullet_price
    print(f"{len(bullets_stack)} bullets left. Earned ${money_earned}")
