def triangle_top(n):
    for row_number in range(1, n+1):
        for number in range(1, row_number+1):
            print(number, end=" ")
        print()


def triangle_bottom(n):
    for row_number in range(n, 1, -1):
        for number in range(1, row_number):
            print(number, end=" ")
        print()


def triangle(n):
    triangle_top(n)
    triangle_bottom(n)

