t = int(input())
while t != 0:
    string = input()
    stack = []
    for i in string:
        if i.isdigit():
            stack.append(i)
        else:
            n2 = int(stack.pop())
            n1 = int(stack.pop())
            output = 0
            if i == "+":
                output = n1 + n2
            elif i == "*":
                output = n1 * n2
            elif i == "-":
                output = n1 - n2
            else:
                output = n1 / n2
            stack.append(output)
    print(stack[0])
    t -= 1

"""
ip->92+51--
op->7
"""
