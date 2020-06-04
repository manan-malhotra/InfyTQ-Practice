def shell_sort(arr):
    sublistcount = len(arr) // 2

    while sublistcount > 0:
        for start in range(sublistcount):
            gap_insertion_sort(arr, start, sublistcount)
        print(arr)
        sublistcount = sublistcount // 2


def gap_insertion_sort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        currentValue = arr[i]
        position = i

        while position >= gap and arr[position - gap] > currentValue:
            arr[position] = arr[position - gap]
            position = position - gap

        arr[position] = currentValue


arr = [12, 44, 66, 22, 99, 0, 23, 66, 11, 55, 2]
shell_sort(arr)
print(arr)
