def sel_sort(arr):
    n = len(arr)

    for i in range(n-1):
        mini = i
        for j in range(i,n):
            if arr[j] < arr[mini]:
                mini = j
        arr[mini], arr[i] = arr[i], arr[mini]
    return arr

arr = [13,43,23,53,9]
print(sel_sort(arr))