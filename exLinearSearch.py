import time
list = [1,2,3,4,5,6,7,8,9,10]

def linearSearch(list, n):
    returnList = []
    for i, j in enumerate(list):
        if j == n:
            returnList.append(i)
    if len(returnList) == 0:
        return False
    else:
        return returnList

start = time.perf_counter()
print(linearSearch(list, 7))
end = time.perf_counter()
print(str((end - start) * 1000) + " ms") 