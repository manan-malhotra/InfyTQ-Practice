t = int(input())
while t != 0:
    num = int(input())
    arr = list(map(int, input().split()))
    total = (num * (num + 1)) / 2
    sum_total = sum(arr)
    print(int(total - sum_total))
    t -= 1

"""
ip-> 5
    1 3 4 5
op-> 2
"""
