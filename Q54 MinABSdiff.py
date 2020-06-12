def minimumAbsoluteDifference(arr):
    arr.sort()
    min_dif = abs(arr[0] - arr[1])
    for i in range(len(arr)-1):
        dif = abs(arr[i] - arr[i+1])
        if dif < min_dif:
            min_dif = dif
    return min_dif


n = int(input())
arr = list(map(int, input().rstrip().split()))
print(minimumAbsoluteDifference(arr))

"""
ip-> 3
     3 -7 0
op-> 3
"""
