number = int(input())

odd_set = set()
even_set = set()

for current_row in range(1, number + 1):
    summed_value = sum(ord(letter) for letter in list(input())) // current_row

    if summed_value % 2 != 0:
        odd_set.add(summed_value)

    else:
        even_set.add(summed_value)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")

elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")

elif sum(odd_set) < sum(even_set):
    print(*odd_set.symmetric_difference(even_set), sep=", ")