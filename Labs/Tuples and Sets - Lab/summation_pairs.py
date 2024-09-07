numbers = list(map(int, input().split()))
target = int(input())

pairs = {}

for num in range(len(numbers)):
    if numbers[num] == "":
        continue
    for n in range(num + 1, len(numbers)):
        if numbers[n] == "":
            continue
        if numbers[num] + numbers[n] == target:
            print(f"{numbers[num]} + {numbers[n]} = {target}")
            numbers[num] = ""
            numbers[n] = ""
            break