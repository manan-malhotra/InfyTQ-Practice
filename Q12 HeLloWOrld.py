string = input()
sort = sorted(set(string.upper()))
# DEHLORW
result = []
for i in range(len(sort)):
    newstr = ""
    for j in string:
        if sort[i] == j.upper():
            newstr += j
    result.append(newstr)
i = 0
j = len(result) - 1
out = ""
while i <= j:
    if i == j:
        out += result[i]
    else:
        out += result[i] + result[j]
    i += 1
    j -= 1
print(out)
