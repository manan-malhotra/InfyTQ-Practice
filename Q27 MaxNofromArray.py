from itertools import permutations

elements = input().split()
p_tuples = permutations(elements)
list_ele = []
for t in p_tuples:
    value = int("".join(t))
    list_ele.append(value)
print(max(list_ele))

"""
ip->13 22 9
op->92213
"""
