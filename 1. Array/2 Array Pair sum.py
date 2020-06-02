def pair(arr,k):
    if len(arr)<2:
        return 

    #sets for tracking
    seen=set()
    output=set()

    #For every number in array
    for num in arr:
        target=k-num

        if target not in seen:  #Puts Target into seen
            seen.add(num)
        else:
            output.add(((min(num,target)),max(num,target)))  #Puts tuple in output
    return "\n".join(map(str,list(output)))

print(pair([1,2,2,3,4,0,5,-1],4))