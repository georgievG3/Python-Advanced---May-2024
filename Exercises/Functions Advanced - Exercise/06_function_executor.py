def func_executor(*args):
    result = []
    for func, numbers in args:
        result.append(f"{func.__name__} - {func(*numbers)}")

    return "\n".join(result)





def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
