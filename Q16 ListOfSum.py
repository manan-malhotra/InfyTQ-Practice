import itertools

input_set = list(map(int, input().split(",")))
s = int(input())
list_combination = list(itertools.combinations(input_set, 4))
print(list_combination)
count = 0
for obj in list_combination:
    ss = sum(obj)
    if ss == s:
        count += 1
print(count)
