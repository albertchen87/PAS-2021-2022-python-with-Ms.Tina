import time

def binarySearch(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, high, x)
    else:
        return -1

arr = [1,2,3,4,5,6,7,8,9,10]
start = time.perf_counter()
result = binarySearch(arr, 0, len(arr) - 1, 10)
end = time.perf_counter()
print(result)
print(str((end - start) * 1000) + " ms")
