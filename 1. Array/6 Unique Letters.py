def unique(s):
    return len(set(s))==len(s)  #A set only adds unique chars

print(unique("ancdss"))


# Manually For Interviews

def unique2(s):
    chars=list()

    for letter in s:
        if letter in chars:
            return False
        else:
            chars.append(letter)
    return True
print(unique2("ancdst"))