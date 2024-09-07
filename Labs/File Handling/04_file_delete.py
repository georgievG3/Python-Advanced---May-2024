import os

file = "my_first_file.txt"

try:
    os.remove(file)

except FileNotFoundError:
    print("File already deleted!")
