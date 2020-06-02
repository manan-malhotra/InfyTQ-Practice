t = int(input())
while t != 0:
    s1 = input().lower()
    s2 = input().lower()
    s1_count = [0] * 26
    s2_count = [0] * 26
    for i in range(len(s1)):
        s1_count[ord(s1[i]) - 97] += 1
    for i in range(len(s2)):
        s2_count[ord(s2[i]) - 97] += 1
    delete = 0
    for i in range(26):
        delete += abs(s1_count[i] - s2_count[i])
    print(delete)
    t -= 1
