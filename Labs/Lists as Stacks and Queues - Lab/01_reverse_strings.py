expression = list(input())
stack = []

while expression:
    stack.append(expression.pop())

print("".join(stack))