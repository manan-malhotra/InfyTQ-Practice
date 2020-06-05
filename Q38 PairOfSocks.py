def sock(n, ar):
    c = 0
    sock = set(ar)
    for i in sock:
        if ar.count(i) % 2 != 0:
            c += 1
    return (n-c)//2


def sock1(n, ar):
    graph = {}
    c = 0
    for i in ar:
        if i in graph:
            graph[i] += 1
        else:
            graph[i] = 1
    for k in graph.values():
        c += k//2
    return c


n = 10
ar = [1, 2, 3, 3, 2, 1, 1, 1, 1, 2]
print(sock(n, ar))
print(sock1(n, ar))
