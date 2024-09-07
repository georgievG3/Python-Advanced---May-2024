def math_operations(*args, **kwargs):
    step = 0
    while step != len(args):
        for key, value in kwargs.items():
            if step == len(args):
                break

            if key == "a":
                kwargs[key] += args[step]

            elif key == "s":
                kwargs[key] -= args[step]

            elif key == "d":
                if args[step] != 0:
                    kwargs[key] /= args[step]

            elif key == "m":
                kwargs[key] *= args[step]

            step += 1

    sorted_dict = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    result = [f"{key}: {value:.1f}" for key, value in sorted_dict]

    return "\n".join(result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
