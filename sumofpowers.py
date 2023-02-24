def sumPowersOf2Iterate(power):
    sum = 0
    for x in range(1, power + 1):
        number = 2 ** x
        sum += number
    return sum


def sumPowersOf2Recursive(power):
    if power == 1:
        return 2 ** power
    else:
        return (2 ** power) + sumPowersOf2Recursive(power - 1)



print(sumPowersOf2Iterate(10))
print(sumPowersOf2Recursive(10))