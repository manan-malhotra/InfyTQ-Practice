n, r = (map(int, input().split()))
ar = list(map(int, input().split()))
a = ar[r:]+ar[:r]
for i in a:
    print(i, end=" ")
