
def bubble(arr):
    n = len(arr)
    swap = False
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if swap:
            swap = False
        else:
            break
    return arr

arr = [10,4,3,1,2,6]
print(bubble(arr))