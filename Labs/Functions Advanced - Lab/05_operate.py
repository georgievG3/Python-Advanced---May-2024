from functools import reduce

def operate(operator, *args):

    def sum_numbers():
        return sum(args)

    def subtract_numbers():
        result = reduce(lambda x, y: x - y, args)
        return result

    def multiplication():
        result = reduce(lambda x, y: x * y, args)
        return result

    def division():
        result = reduce(lambda x, y: x / y, args)
        return result

    if operator == "+":
        return sum_numbers()

    elif operator == "-":
        return subtract_numbers()

    elif operator == "*":
        return multiplication()

    elif operator == "/":
        return division()


print(operate("*", 3, 4))
