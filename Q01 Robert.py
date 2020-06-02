list = input().split(",")
out = ""
for i in list:
    temp = i.split(":")
    name = temp[0]
    number = temp[1]
    l = len(name)
    max = 0
    for j in number:
        if int(j) <= l:
            if max < int(j):
                max = int(j)
    if max == 0:
        out += "X"
    else:
        out += name[max - 1]
print(out)
