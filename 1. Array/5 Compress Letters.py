def compress(s):
    r=""
    if len(s)==0:
        return 0
    if len(s)==1:
        return s+"1"
    last=s[0]
    i=1
    count=1
    length=len(s)
    while i<length:

        if s[i]==s[i-1]:
            count+=1
        else:
            r=r+s[i-1]+str(count)
            count=1
        i+=1
    r=r+s[i-1]+str(count)
    return r


print(compress("AabbBB"))