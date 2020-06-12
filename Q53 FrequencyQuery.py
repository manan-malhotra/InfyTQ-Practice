from collections import defaultdict, deque
q = int(input())
arr = defaultdict(int)
out = deque()
freq = defaultdict(set)
for _ in range(q):
    o, n = map(int, input().split())
    if o == 1:
        v = arr[n]
        arr[n] = v + 1
        if n in freq[v]:
            freq[v].remove(n)
        freq[v + 1].add(n)
    elif o == 2:
        v = arr[n]
        if v > 0:
            v = arr[n]
            arr[n] = v - 1
            if n in freq[v]:
                freq[v].remove(n)
            freq[v - 1].add(n)
    else:
        if freq[n]:
            out.append(1)
        else:
            out.append(0)
for i in out:
    print(i)

"""
ip->
8
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2
op->
0
1

You are given  queries. Each query is of the form two integers described below:
1-x  : Insert x in your data structure.
2-y  : Delete one occurence of y from your data structure, if present.
3-z  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.
"""
