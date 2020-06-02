t = int(input())
while t != 0:
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = l1.copy()
    l2.sort()
    d = {}
    for i in range(n):
        d[l2[i]] = i
    for j in range(n):
        print(d[l1[j]], end=" ")
    print()
    t -= 1
