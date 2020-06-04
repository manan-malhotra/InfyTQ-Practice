"""
todo Implement Sequential ordered search
"""


def ordered_seq_search(arr, element):
    position = 0
    found = False
    stopped = False
    while position < len(arr) and not found and not stopped:
        if arr[position] == element:
            found = True
        else:
            if arr[position] > element:
                stopped = True
            else:
                position += 1

    return found


arr = [1, 2, 3, 4, 5, 8, 9, 10]
n = int(input())
print(ordered_seq_search(arr, n))


def unordered_seq_search(arr, element):
    position = 0
    found = False
    stopped = False
    while position < len(arr) and not found and not stopped:
        # print(position)
        if arr[position] == element:
            found = True
        else:
            position += 1
    return found


a = [1, 7, 10, 3, 4, 9]
print(unordered_seq_search(a, n))
