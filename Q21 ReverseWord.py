t = int(input())
while t != 0:
    string = input()
    list_string = string.split(".")
    list_string.reverse()
    print(".".join(list_string))
    t -= 1
