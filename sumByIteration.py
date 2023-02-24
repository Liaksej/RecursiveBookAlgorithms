def sum_iterative(number):
    """Iterative Factorial Algorithm."""
    product = 0
    for i in range(1, number + 1):
        product = product + i
    return product


def sum_recursive(number):
    if number == 1:
        # BASE CASE
        return 1
    else:
        # RECURSIVE CASE
        return number + sum_recursive(number - 1)


print(sum_iterative(5))
print(sum_recursive(10))

