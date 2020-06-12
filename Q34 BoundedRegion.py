import re

t = int(input())
while t != 0:
    n = int(input())
    words = input()
    ones = re.findall("[abdegopq4690ADOPQR]", words)
    twos = re.findall("[B8]", words)
    print(len(ones) + (len(twos) * 2))
    t -= 1


"""
ip->BS0
op->3
"""
