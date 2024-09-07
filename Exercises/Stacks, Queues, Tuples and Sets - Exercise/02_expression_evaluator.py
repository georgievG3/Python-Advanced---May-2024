from functools import reduce

def evaluate_expression(expression):
    tokens = expression.split()
    numbers = []

    for token in tokens:
        if token in {"*", "+", "-", "/"}:
            if token == "*":
                result = reduce(lambda x, y: x * y, numbers)
            elif token == "+":
                result = reduce(lambda x, y: x + y, numbers)
            elif token == "-":
                result = reduce(lambda x, y: x - y, numbers)
            elif token == "/":
                result = reduce(lambda x, y: x // y, numbers)

            numbers = [result]
        else:
            numbers.append(int(token))

    return numbers[0]


expression = input().strip()
print(evaluate_expression(expression))
