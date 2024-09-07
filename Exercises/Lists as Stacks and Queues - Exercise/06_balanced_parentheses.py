from collections import deque

parentheses = deque(list(input()))

opening_parentheses = "({["
closing_parentheses = ")}]"

matching_pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

opening_stack = []

for char in parentheses:

    if char in opening_parentheses:
        opening_stack.append(char)

    elif char in closing_parentheses:
        if not opening_stack or opening_stack[-1] != matching_pairs[char]:
            print("NO")
            break

        opening_stack.pop()

else:

    if opening_stack:
        print("NO")

    else:
        print("YES")
