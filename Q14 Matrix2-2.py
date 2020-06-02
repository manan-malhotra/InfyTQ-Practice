def isdiv(n):
    s = sum(list(map(int, str(n))))
    if n % s == 0:
        return True
    return False


row = int(input())
m = []
for r in range(row):
    m.append(list(map(int, input().split())))
col = len(m[0])
for r in range(row - 1):
    for c in range(col - 1):
        if (
            isdiv(m[r][c])
            and isdiv(m[r][c + 1])
            and isdiv(m[r + 1][c])
            and isdiv(m[r + 1][c + 1])
        ):
            print(f"{(m[r][c])} {(m[r][c+1])}")
            print(f"{(m[r+1][c])} {(m[r+1][c+1])}")
