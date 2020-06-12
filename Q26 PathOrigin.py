from math import factorial

t = int(input())
while t != 0:
    x, y = map(int, input().split())
    a = factorial(x + y)
    b = factorial(x) * factorial(y)
    print(a // b)
    t -= 1

"""
Matrix no of distances
ip->3 4
op->35
"""
