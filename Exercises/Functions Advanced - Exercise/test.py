my_tuple = (2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish")

cubes_total = [int(n) for n in my_tuple[3:] if isinstance(n, int)]

print(sum(cubes_total))