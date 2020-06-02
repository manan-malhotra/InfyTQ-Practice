ip = input()
l1 = ip.split(",")
string = l1[0]
ch = l1[1]
substr = string.split(ch)
total = 0
for s in substr:
    l = len(s)
    total += (l + (l + 1)) / 2
print(int(total))
