def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swap = False
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swap = True
        if not swap:
            break
        print("run")
    return arr

arr = [13,43,23,53,9]
arr = [1,2,3,4,5]
print(bubble_sort(arr))