def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return -1


print(finder([1, 2, 3, 4, 5, 6], [6, 3, 4, 2, 1]))

# Second Solution

from collections import defaultdict


def finder2(arr1, arr2):
    d = defaultdict(int)

    for num in arr2:
        d[num] += 1
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


print(finder2([1, 2, 3, 4, 7, 6], [6, 3, 4, 2, 1]))

# Can also Find sum of both arrays and subtract them to get the number
# But it can be problematic for large numbers

# CLEVER TRICK


def finder3(arr1, arr2):
    result = 0
    for num in arr1 + arr2:
        result ^= num  # XOR both list: IN XOR 1^1=0 0^1=1
        # print(result)
    return result


print(finder3([1, 2, 3], [2, 3]))

