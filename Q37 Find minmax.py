n = int(input())
l1 = list(map(int, input().split()))
min = min(l1)
max = max(l1)
total = sum(l1)
print(total - max, end=" ")
print(total - min)

"""
ip->3
ip->2 3 4
op->5 7
"""
