from collections import deque

tools = deque(int(x) for x in input().split())
substances_as_stack = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while substances_as_stack and tools and challenges:

    tool = tools.popleft()
    substance = substances_as_stack.pop()

    result = tool * substance

    if result in challenges:
        challenges.remove(result)

    else:
        tools.append(tool + 1)

        substance -= 1

        if substance > 0:
            substances_as_stack.append(substance)

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")

if substances_as_stack:
    print(f"Substances: {', '.join([str(x) for x in substances_as_stack])}")

if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")