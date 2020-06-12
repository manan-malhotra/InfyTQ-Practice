n = int(input())
list1 = list(map(int, input().split()))
k = int(input())
m = max(list1)
count = [0]*(m+1)
for i in list1:
    count[i] += 1
for i in range(m+1):
    if(count[i] == k):
        print(i)
        break

"""
ip-> 11 11 11 2 2
ip->3
op->11
"""
