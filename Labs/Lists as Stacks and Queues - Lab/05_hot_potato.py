from collections import deque

queue = deque(input().split())
toss = int(input())

while len(queue) > 1:

    for n in range(toss - 1):
        queue.append(queue.popleft())

    print(f"Removed {queue.popleft()}")

print(f"Last is {queue.pop()}")

