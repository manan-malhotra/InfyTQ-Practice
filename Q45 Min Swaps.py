n = int(input())
arr = list(map(int, input().split()))
swaps = 0

for i in range(0, n - 1):
    while arr[i] != i + 1:
        arr[arr[i]-1],arr[i]=arr[i],arr[arr[i]-1]
        swaps += 1

print(swaps)
#  4 3 1 2