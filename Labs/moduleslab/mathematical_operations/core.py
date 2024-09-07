def divide_nums(n1, n2):
    return f"{n1 / n2:.2f}"


def multiply_nums(n1, n2):
    return f"{n1 * n2:.2f}"


def subtract_nums(n1, n2):
    return f"{n1 - n2:.2f}"


def add_nums(n1, n2):
    return f"{n1 + n2:.2f}"


def raise_nums(n1, n2):
    return f"{n1 ** n2:.2f}"


mapper = {
    "/": divide_nums,
    "*": multiply_nums,
    "-": subtract_nums,
    "+": add_nums,
    "^": raise_nums
}
