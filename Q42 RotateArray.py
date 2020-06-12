n, r = (map(int, input().split()))
ar = list(map(int, input().split()))
a = ar[r:]+ar[:r]
for i in a:
    print(i, end=" ")

"""
ip->5 4
ip->1 2 3 4 5
op->5 1 2 3 4
"""
