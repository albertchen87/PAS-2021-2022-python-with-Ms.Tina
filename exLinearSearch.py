import time
list = [6,5,4,3,2,1,3,3,3,3,3,4]

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
print((end - start) * 1000)