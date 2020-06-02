num = input().split(",")
five = num.index("5")
eight = num.index("8")
n1 = 0
n2 = ""
length = len(num)
for i in range(five, eight + 1):
    n2 += "".join(num[i])
for i in range(length):
    if i < five or i > eight:
        n1 += int(num[i])
print(n1 + int(n2))

