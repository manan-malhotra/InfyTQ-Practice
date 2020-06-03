def permutate(s):
    out = []
    # BASE
    if len(s) == 1:
        out = [s]

    else:
        for i, let in enumerate(s):
            for perm in permutate(s[:i] + s[i + 1 :]):
                out += [let + perm]
    return out


print(permutate("abcd"))
