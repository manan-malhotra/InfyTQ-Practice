def binary(arr, ele):
    if len(arr) == 0:
        print("Not found")
    else:
        half = (len(arr)) // 2
        if arr[half] == ele:
            print("Found")
        elif arr[half] < ele:
            binary(arr[half + 1 :], ele)
        elif arr[half] > ele:
            binary(arr[:half], ele)


arr = [1, 3, 6, 7, 9, 12, 19, 24, 40, 51]
(binary(arr, 51))
