test_cases = int(input())

for _ in range(test_cases):
    t = int(input())
    a = list(map(int, input().split()))
    swaps = [0] * t

    swapped = True

    while swapped:
        swapped = False

        for i in range(t):
            while i < t - 1 and a[i] > a[i + 1]:
                swaps[a[i] - 1] += 1
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
                i += 1

    s = 0
    for swap in swaps:
        s += swap

        if swap > 2:
            print('Too chaotic')
            break
    else:
        print(s)


"""
ip->
2
5
2 1 5 3 4
5
2 5 1 3 4
op->
3 too chaotic
"""
