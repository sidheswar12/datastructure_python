
def binarysearch(arr, beg, end, elm):
    count = 0  
    while beg<=end:
        count += 1
        mid = beg + (end - beg) // 2                  
        if arr[mid] == elm:
            return mid
        elif arr[mid] < elm:
            beg = mid + 1
        else:
            end = mid - 1    
    return -1


def lenearsearch(arr, elm):
    for idx, item in enumerate(arr):
        if item == elm:
            return idx
    return -1


arr = [1,5,6,8,9,10,20,22,25]
res = binarysearch(arr, 0, len(arr) - 1, 10)
if res !=-1:
    print("{} is present in index {}".format(10, res))
else:
    print("{} is not present in list".format(10))


arr1 = [20, 21, 4, 5, 2, 6, 8, 1, 7, 6, 8, 9, 10, 20, 22, 25]
rs = lenearsearch(arr1, 5)
if rs !=-1:
    print("{} is present in index {}".format(5, rs))
else:
    print("{} is not present in list".format(5))