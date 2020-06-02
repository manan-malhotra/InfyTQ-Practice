n = input()
otp = ""
l = len(n)
for i in range(1, l, 2):
    num = int(n[i]) ** 2
    otp += str(num)
print(otp[:4])
