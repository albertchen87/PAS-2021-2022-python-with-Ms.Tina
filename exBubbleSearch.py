<<<<<<< Updated upstream
 
=======
def enterArr():
    s = input("Enter array")
    arr = s.split()
    return arr

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selectionSort(arr):
    for i in range(len(arr)):
        index = i
        for j in range(len(arr) - 1):
            if arr[i] > arr[j]:
                cindex = j
        arr[i], arr[j] = arr[j], arr[i]

a = bubbleSort(enterArr())

for i in a:
    print(i + " ", end = "")

b = selectionSort(enterArr())

for i in b:
    print(i + " ", end = "")
>>>>>>> Stashed changes
