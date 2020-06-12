rem = int(input())
list_num = list(map(int, input().split(" ")))
list_element_count = []
set_distinct = set(list_num)
for i in set_distinct:
    count = list_num.count(i)
    list_element_count.append(count)
list_element_count.sort()
length = len(list_element_count)
for count in list_element_count:
    if count <= rem:
        rem -= count
        length -= 1
    else:
        break
print(length)

"""
Min distinct no after removal
ip-> 2 
ip-> 1 2 2 1 3 3
op-> 2
"""
