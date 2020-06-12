def substrCount(n, s):
    tot = 0
    count_sequence = 0
    prev = ''
    for i, v in enumerate(s):
        count_sequence += 1
        if i and (prev != v):
            j = 1
            while ((i-j) >= 0) and ((i+j) < len(s)) and j <= count_sequence:
                if s[i-j] == prev == s[i+j]:
                    tot += 1
                    j += 1
                else:
                    break
            count_sequence = 1
        tot += count_sequence
        prev = v
    return tot


n = int(input())
s = input()
result = substrCount(n, s)
print(result)
# aabaa
# 9

"""
ip-> asasd
op-> 7
a,s,a,s,d,asa,sas
"""
