def fib_rec(n):

    # Base Case
    if n < 2:
        return n
    else:
        # recursion
        return fib_rec(n - 1) + fib_rec(n - 2)


print(fib_rec(10))


def fib_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fib_iter(10))
