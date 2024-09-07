from collections import deque

tasks_time = deque(int(x) for x in input().split())
number_of_tasks = [int(x) for x in input().split()]

rubber_ducks_types = {
    "Darth Vader Ducky": [0, 60],
    "Thor Ducky": [61, 120],
    "Big Blue Rubber Ducky": [121, 180],
    "Small Yellow Rubber Ducky": [181, 240]
}

collected_ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}
highest_range = rubber_ducks_types["Small Yellow Rubber Ducky"][1]

while tasks_time and number_of_tasks:

    calculated_time = tasks_time[0] * number_of_tasks[-1]

    if calculated_time > highest_range:
        number_of_tasks[-1] -= 2
        tasks_time.append(tasks_time.popleft())
        continue

    for duck_name, time_needed in rubber_ducks_types.items():

        if time_needed[0] <= calculated_time <= time_needed[1]:

            collected_ducks[duck_name] += 1
            tasks_time.popleft()
            number_of_tasks.pop()

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for k, v in collected_ducks.items():
    print(f"{k}: {v}")
