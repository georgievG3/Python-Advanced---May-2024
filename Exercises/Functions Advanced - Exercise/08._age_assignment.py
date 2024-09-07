def age_assignment(*args, **kwargs):
    result = []
    for name in args:
        result.append(f"{name} is {kwargs[name[0]]} years old.")


    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))

