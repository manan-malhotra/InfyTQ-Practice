from itertools import permutations

t = int(input())
while t != 0:
    string = input()
    list_tuples = permutations(string)
    p_list = []
    for i in list_tuples:
        joinstring = "".join(i)
        p_list.append(joinstring)
    p_list.sort()
    for i in p_list:
        print(i, end=" ")
    print()
    t -= 1

"""
ip-> abc
op-> abc acb bac bca cab cba
"""
