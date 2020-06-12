n, m = map(int, input().split())
s1 = input().split(" ")
s2 = input().split(" ")
s = {}
for i in s1:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
same = 0
for i in s2:
    if i in s:
        if s[i] > 0:
            s[i] -= 1
        else:
            same += 1
    else:
        same += 1
if same == 0:
    print("Yes")
else:
    print("No")

"""
ip-> give me five hundred
ip-> give me hundred
op-> Yes
"""
