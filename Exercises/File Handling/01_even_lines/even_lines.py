with open("text.txt") as file:

    text = file.readlines()

    for row, line in enumerate(text):
        if row % 2 == 0:
            for ch in "-,.!?":
                if ch in line:
                    line = line.replace(ch, "@")
            print(" ".join(reversed(line.split())))
