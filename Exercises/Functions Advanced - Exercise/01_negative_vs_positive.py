def sum_nums(*args):
    negative_sum = sum(n for n in args if n < 0)
    positive_sum = sum(n for n in args if n > 0)

    return negative_sum, positive_sum


numbers = [int(n) for n in input().split()]
n_sum, p_sum = sum_nums(*numbers)
print(n_sum)
print(p_sum)

if abs(n_sum) > p_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
