number = int(input())

usernames = set()

for n in range(number):
    name = input()

    usernames.add(name)

print(*usernames, sep="\n")
