from Labs.moduleslab.fibonacci_sequence.core import create_sequence, locate_number

seq = None
while True:
    command = input()

    if command == "Stop":
        break

    tasks = command.split()

    if tasks[0] == "Create":
        count = int(tasks[2])

        seq = create_sequence(count)
        print(*seq, sep=" ")

    elif tasks[0] == "Locate":
        number = int(tasks[1])

        if number in seq:
            print(f"The number - {number} is at index {locate_number(seq, number)}")

        else:
            print(f"The number {number} is not in the sequence")


