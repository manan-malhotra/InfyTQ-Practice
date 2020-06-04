def selectionSort(arr):

    for fillslot in range(len(arr) - 1, 0, -1):
        positionOfMax = 0

        for location in range(1, fillslot + 1):
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location

        arr[fillslot], arr[positionOfMax] = arr[positionOfMax], arr[fillslot]

    print(arr)


arr = [5, 8, 3, 2]
# selectionSort(arr)

# ! Easier Way


def selection(arr):
    for i in range(len(arr)):
        lowest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest]:
                lowest = j
        arr[i], arr[lowest] = arr[lowest], arr[i]
    return arr


print(selection(arr))
