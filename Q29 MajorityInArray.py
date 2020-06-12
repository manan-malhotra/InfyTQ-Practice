# t = int(input())
# while t != 0:
#     n = int(input())
#     l = list(map(int, input().split()))
#     half = n // 2
#     s = set(l)
#     op = -1
#     for i in s:
#         if l.count(i) > half:
#             op = i
#     print(op)
#     t -= 1
t = int(input())
while t != 0:
    n = int(input())
    l = list(map(int, input().split()))
    m = max(l)
    count_list = [0] * (m + 1)
    for i in l:
        count_list[i] += 1
    max_val = max(count_list)
    if max_val > n / 2:
        idx = count_list.index(max_val)
        print(idx)
    else:
        print(-1)
    t -= 1


"""
ip->7
ip->1 2 2 2 2 3 3
op->2
"""
