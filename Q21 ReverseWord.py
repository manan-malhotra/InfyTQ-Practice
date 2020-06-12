t = int(input())
while t != 0:
    string = input()
    list_string = string.split(".")
    list_string.reverse()
    print(".".join(list_string))
    t -= 1

"""
ip-> I.am.a.boy
op-> boy.a.am.I
"""
