# t = int(input())
# while t != 0:
#     num = list(input())
#     c = num.count("1")
#     op = c * (c - 1)
#     print(op // 2)
#     t -= 1
t = int(input())
num_list = []
for i in range(t):
    num_list.append(list(input()))
for num in num_list:
    c = num.count("1")
    op = c * (c - 1)
    print(op // 2)

"""
find total number of pair starting and ending with 1
ip-> 1101
op-> 3
"""
