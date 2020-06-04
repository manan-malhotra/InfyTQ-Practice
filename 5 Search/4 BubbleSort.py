

def bubbleSort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for k in range(n):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
        print(arr)

#todo   visualgo.net

arr = [2, 5, 9, 3, 7, 22, 6]
bubbleSort(arr)
