def insertionSort(arr):

    for i in range(1, len(arr)):
        current = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > current:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = current
    print(arr)


arr = [4, 8, 2, 9, 1, 7]
insertionSort(arr)
