num = int(input())
for i in range(1, num + 1):
    a = str(i * (i + 1))
    if a in str(num):
        print(a)
