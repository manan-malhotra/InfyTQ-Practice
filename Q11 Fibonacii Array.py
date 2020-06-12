list_num = list(map(int, input().split(",")))
list_num.sort()
length = len(list_num)
list_total = []
for i in range(length):
    for x in range(i + 1, length):
        first = list_num[i]
        second = list_num[x]
        f_list = []
        f_list.append(first)
        f_list.append(second)
        for y in range(x + 1, length):
            if first + second == list_num[y]:
                f_list.append(list_num[y])
                first = second
                second = list_num[y]
                if len(list_total) < len(f_list):
                    list_total = f_list
if len(list_total) > 2:
    print(list_total)
else:
    print(-1)


"""
ip-> 2,3,4,6,8
op-> [2,4,6]
"""
