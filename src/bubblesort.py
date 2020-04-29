
def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        print (arr)

def main():
    arr = [6, 3, 2, 1, 7, 9, 5, 2, 4, 0]
    bubbleSort(arr)
    print("Sorted Array: ", arr)


if __name__ == "__main__":
    main()