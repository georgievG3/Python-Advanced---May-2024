def create_sequence(n):
    sequence = [0, 1]

    for number in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


def locate_number(sequence, n):
    return sequence.index(n)


