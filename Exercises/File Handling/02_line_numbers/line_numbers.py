from string import punctuation

with open("text.txt") as file, open("output.txt", "w") as f:

    result = []

    for row, line in enumerate(file):
        letters_count = 0
        punct_count = 0

        for ch in line:

            if ch.isalpha():
                letters_count += 1

            elif ch in punctuation:
                punct_count += 1

        result.append(f"Line {row + 1}: {line.strip()} ({letters_count})({punct_count})")

    f.write("\n".join(result))
