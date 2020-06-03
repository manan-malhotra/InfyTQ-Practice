def reverse(s):
    # Base Case
    if len(s) == 1:
        return s
    # Recursive Case
    return reverse(s[1:]) + s[0]


print(reverse("Kya re "))
