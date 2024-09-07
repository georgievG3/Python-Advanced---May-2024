from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars_queue = deque()
passed_cars = 0
crashed = False

while True:
    command = input()

    if command == "END":
        break

    elif command == "green":
        if cars_queue:
            current_car = cars_queue.popleft()
            seconds_left = green_light_duration - len(current_car)

            while seconds_left > 0:
                passed_cars += 1

                if cars_queue:
                    current_car = cars_queue.popleft()
                    seconds_left -= len(current_car)

                else:
                    break

            if seconds_left == 0:
                passed_cars += 1

            if free_window_duration >= abs(seconds_left):
                if seconds_left < 0:
                    passed_cars += 1

            else:
                index = free_window_duration + seconds_left
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[index]}.")
                crashed = True
                break
    else:
        cars_queue.append(command)

if not crashed:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")



