def fill_the_box(height, length, width, *args):

    free_space = height * length * width

    cubes_total = sum([n for n in args[3:] if isinstance(n, int)])
    for cube in args[3:]:

        if cube == "Finish":
            if free_space:
                return f"There is free space in the box. You could put {free_space} more cubes."
            return f"No more free space! You have {cubes_total} more cubes."

        if cube <= free_space:
            free_space -= cube
            cubes_total -= cube

        else:
            last_space = free_space
            free_space = 0
            cubes_total -= last_space


print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
