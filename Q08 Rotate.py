dic = input().split(",")
for obj in dic:
    str_obj = obj.split(":")
    string = str_obj[0]
    num = str_obj[1]
    length = len(string)
    sum = 0
    for digit in num:
        sum += int(digit) ** 2
    if sum % 2 == 0:
        s = string[-1]
        print(s + string[: length - 1], end=" ")
    else:
        s = string[:2]
        print(string[2:] + s, end=" ")
