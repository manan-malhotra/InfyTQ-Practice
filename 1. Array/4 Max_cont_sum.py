def max_cont_sum(arr):

    if len(arr)==0:
        return 0
    
    max_sum=curr_sum=arr[0]
    
    for num in arr[1:]:
        curr_sum=max(curr_sum+num,num)
        max_sum=max(curr_sum,max_sum)
    return max_sum

print(max_cont_sum([-14,-2,-2,-1,-10,-10,-3,-30]))