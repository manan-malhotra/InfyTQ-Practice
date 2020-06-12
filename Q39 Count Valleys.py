def valleys(n, string):
    level = valley = 0
    for i in range(n):
        if string[i] == "U":
            level += 1
            if level == 0:
                valley += 1
        else:
            level -= 1
    return valley


n = 6
string = "UDDUDU"
print(valleys(n, string))


"""
ip-> 8
ip-> UDDDUDUU
op->1
"""
