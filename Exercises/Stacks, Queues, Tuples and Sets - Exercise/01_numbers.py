first_seq = set(map(int, input().split()))
second_seq = set(map(int, input().split()))

number = int(input())

for line in range(number):
    command = input().split()

    command_type = command[0]
    seq_type = command[1]
    numbers = set(map(int, command[2:]))

    if command_type == "Add":

        if seq_type == "First":
            first_seq.update(numbers)

        elif seq_type == "Second":
            second_seq.update(numbers)

    elif command_type == "Remove":

        if seq_type == "First":
            first_seq.difference_update(numbers)

        elif seq_type == "Second":
            second_seq.difference_update(numbers)

    elif command_type == "Check":

        if first_seq.issubset(second_seq) or second_seq.issubset(first_seq):
            print("True")
        else:
            print("False")

print(", ".join(map(str, sorted(first_seq))))
print(", ".join(map(str, sorted(second_seq))))
