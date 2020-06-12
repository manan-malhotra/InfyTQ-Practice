import math

list_num = input().split(",")
digit_sum_list = []
for num in list_num:
    digit_sum = sum(list(map(int, num)))
    digit_sum_list.append(digit_sum)
max_sum = max(digit_sum_list)
list_digit_count = [0] * (max_sum + 1)
for num in digit_sum_list:
    list_digit_count[num] += 1
total_pair = 0
for count in list_digit_count:
    if count > 1:
        total_pair += int(math.factorial(count) /
                          (math.factorial(count - 2) * 2))
if total_pair == 0:
    print(-1)
else:
    print(total_pair)

"""
ip-> 22,4,10,1,23,14
op-> 3
op= no of times when sum is same bw 2 no
"""
