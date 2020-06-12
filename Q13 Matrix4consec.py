row, col = map(int, input().split(" "))
list_digit = []
m = []
for r in range(row):
    row_numbers = list(map(int, input().split()))
    m.append(row_numbers)
for r in range(row):
    for c in range(col):
        if c < col - 3:
            if m[r][c] == m[r][c + 1] == m[r][c + 2] == m[r][c + 3]:
                list_digit.append(m[r][c])
        if r < row - 3:
            if m[r][c] == m[r + 1][c] == m[r + 2][c] == m[r + 3][c]:
                list_digit.append(m[r][c])
        if r >= 3 and c < col - 3:
            if m[r][c] == m[r - 1][c + 1] == m[r - 2][c + 2] == m[r - 3][c + 3]:
                list_digit.append(m[r][c])
        if r >= 3 and c >= 3:
            if m[r][c] == m[r - 1][c - 1] == m[r - 2][c - 2] == m[r - 3][c - 3]:
                list_digit.append(m[r][c])
if len(list_digit) == 0:
    print(-1)
else:
    print(list_digit)
    print(min(list_digit))

"""
ip-> 6 6 
    Matrix of 6*6
op-> Smallest consecutive
"""


"""
ip->6 6
1 1 1 1 2 2
2 2 2 1 2 1
1 2 3 2 2 1
4 2 3 1 2 1
2 2 3 1 1 2
2 2 3 2 2 2
op-> [1, 2, 2, 2, 3, 2]
1
"""
