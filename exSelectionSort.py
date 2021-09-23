def SelectionSort(arr):
    for i in range(len(arr)):
        index = i
        for j in range(i + 1, len(arr)):
            if arr[index] > arr[j]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr

arr = [5,3,4,7,8,2,8,0]

arr = SelectionSort(arr)
for i in range(len(arr)):
    print("%d" % arr[i])