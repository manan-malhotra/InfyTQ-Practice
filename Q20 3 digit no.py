import itertools

num = input().split(",")
out = ""
l = len(num)
s = set(itertools.permutations(num, 3))
max_no = max(s)
leng = len(s)
for i in max_no:
    out += i
print(f"{out},{leng}")

"""
ip-> 2,5,7
op-> 752,6
752 highest number
6 no of combinations
"""
