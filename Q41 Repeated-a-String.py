s = input()
n = int(input())
number = s.count('a')
if number == 0:
    print(0)
elif number == 1 and len(s) == 1:
    print(n)
else:
    repeats = n//len(s)
    remainders = n % len(s)
    print(str(number*repeats+s[:remainders].count('a')))

"""
ip-> aba
ip-> 10
op-> 7
"""
