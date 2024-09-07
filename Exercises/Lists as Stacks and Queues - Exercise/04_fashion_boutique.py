clothes_stack = list(map(int, input().split()))
rack_capacity = int(input())

racks_count = 1
value_sum = 0

while clothes_stack:

    clothing = clothes_stack.pop()

    if value_sum + clothing <= rack_capacity:
        value_sum += clothing

    else:
        racks_count += 1
        value_sum = clothing

print(racks_count)
