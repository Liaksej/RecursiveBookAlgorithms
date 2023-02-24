def factorial_iterative(number):
    """Iterative Factorial Algorithm."""
    product = 1
    for i in range(1, number + 1):
        product = product * i
    return product


def factorial_recursive(number):
    if number == 1:
        # BASE CASE
        return 1
    else:
        # RECURSIVE CASE
        return number * factorial_recursive(number - 1)


# print(factorial_iterative(5))
print(factorial_recursive(5))

