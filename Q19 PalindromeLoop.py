def palin(n):
    if n == n[::-1]:
        return n
    else:
        n = str(int(n) + int(n[::-1]))
        return palin(n)


print(palin(input()))
