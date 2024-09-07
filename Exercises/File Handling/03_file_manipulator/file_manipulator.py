import os

while True:
    line = input()

    if line == "End":
        break

    command, file, *args = line.split("-")

    if command == "Create":
        open(file, "w").close()

    elif command == "Add":
        with open(file, "a") as f:
            f.write(f"{args[0]}\n")

    elif command == "Replace":

        try:
            with open(file, "r+") as f:
                text = f.read()
                f.seek(0)
                f.truncate(0)
                f.write(text.replace(args[0], args[1]))

        except FileNotFoundError:
            print(f"An error occurred")

    elif command == "Delete":

        if os.path.exists(file):
            os.remove(file)

        else:
            print(f"An error occurred")
