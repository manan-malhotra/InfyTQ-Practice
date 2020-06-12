string = input()
even = []
odd = []
special = 0
for char in string:
    if char.isalnum() == False:
        special += 1
    elif char.isdigit():
        if int(char) % 2 == 0:
            even.append(char)
        else:
            odd.append(char)
if special % 2 != 0:
    even, odd = odd, even
even_len = len(even)
odd_len = len(odd)
m = max(even_len, odd_len)
e = 0
o = 0
for i in range(m):
    if e < even_len:
        print(even[e], end="")
        e += 1
    if o < odd_len:
        print(odd[o], end="")
        o += 1

"""
ip-> djbs^%&12345
op-> if no of spcl char is odd start with odd else even

"""
