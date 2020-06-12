string = input()
length = len(string)
half = length // 2
for i in range(half, 0, -1):
    prefix = string[0:i]
    suffix = string[length - i: length]
    if prefix == suffix:
        print(len(suffix))
        break
else:
    print(-1)

"""
ip-> abcdabc
op->3    
(abc)
"""
