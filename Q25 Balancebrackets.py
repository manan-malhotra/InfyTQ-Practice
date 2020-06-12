bracket = input()
left = 0
right = 0
for x in bracket:
    if x == "(":
        left += 1
    else:
        right += 1
print(abs(left - right))

"""
Print no of brackets to delete 
ip->()((
op->2
"""
