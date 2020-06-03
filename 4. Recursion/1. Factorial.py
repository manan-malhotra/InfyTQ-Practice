# Without Recursion


def fact(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


print(fact(5))

# With Recursion


def factrec(n):
    if n == 0:
        return 1
    return n * factrec(n - 1)


print(factrec(5))
