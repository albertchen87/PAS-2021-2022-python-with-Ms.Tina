def SelectionSort(arr):
    print(len(arr))
    for i in range(len(arr)):
        index = i
        for j in range(i + 1, len(arr)):
            if arr[index] > arr[j]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr

def enterArr():
    s = input("Enter array")
    arr = s.split(" ")
    return arr

arr = enterArr()
arrNew = [int(x) for x in arr]
arrNew = SelectionSort(arrNew)
print(arrNew)