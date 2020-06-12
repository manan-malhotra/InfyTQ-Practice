def check(string):
    length = len(string)
    str1 = list(string)
    for i in range(1, length):
        if str1[i] == "#":
            for j in range(i - 1, -1, -1):
                if str1[j].isalpha():
                    if str1[j] == "Z":
                        str1[j] = "A"
                        break
                    else:
                        str1[j] = chr(ord(str1[j]) + 1)
                        break
    return "".join(str1)


t = int(input())
while t != 0:
    str1 = input()
    str2 = input()
    s1 = check(str1)
    s2 = check(str2)
    string1 = "".join(s1.split("#"))
    string2 = "".join(s2.split("#"))
    if string1 == string2:
        print("Yes")
    else:
        print("No")
    t -= 1

"""
ip->
op->
"""