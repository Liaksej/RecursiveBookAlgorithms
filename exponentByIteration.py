def exponentsByIteration(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result


print(exponentsByIteration(3, 6))
print(exponentsByIteration(10, 3))
print(exponentsByIteration(17, 10))