
def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        larr = arr[:mid]
        rarr = arr[mid:]
        mergeSort(larr)
        mergeSort(rarr)
        i = 0
        j = 0
        k = 0
        while i<len(larr) and j<len(rarr):
            if(larr[i]<rarr[j]):
                arr[k] = larr[i]
                i += 1
            else:
                arr[k] = rarr[j]
                j += 1
            k += 1
        while i<len(larr):
            arr[k]=larr[i]
            i += 1
            k += 1
        
        while j<len(rarr):
            arr[k]=rarr[j]
            j += 1
            k += 1
        

def main():
    arr = [6, 3, 2, 1, 7, 9, 5, 2, 4, 0, 1, 3]
    mergeSort(arr)
    print("Sorted Array: ", arr)


if __name__ == "__main__":
    main()