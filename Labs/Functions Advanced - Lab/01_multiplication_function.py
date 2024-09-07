from functools import reduce

def multiply(*args):
    result = reduce(lambda x, y: x*y, args)

    return result
print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))

# def multiply(*args):
#     result = 1
#     for num in args:
#         result *= num
#
#     return result
#
# print(multiply(1, 4, 5))
# print(multiply(4, 5, 6, 1, 3))
# print(multiply(2, 0, 1000, 5000))