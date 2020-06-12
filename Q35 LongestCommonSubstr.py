t = int(input())
while t != 0:
    n1, n2 = list(map(int, input().split()))
    str1 = input()
    str2 = input()
    common = 0
    for i in range(n1):
        for x in range(i + 1, n1 + 1):
            s = str1[i:x]
            length = len(s)
            if s in str2:
                if length > common:
                    common = length
    print(common)
    t -= 1


"""
ip->4 5
ip->abcd
ip->cdefg
op->2
"""
