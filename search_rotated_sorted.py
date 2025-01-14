def search(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == target:
            return mid

        if arr[low] <= arr[mid]:
            if arr[low] <= target and target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= target and target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


# arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
# target = 1
# arr = [4,5,6,7,0,1,2]
# target = 3
arr = [4,5,6,7,0,1,2,3]
# arr.sort()
target = 4
print(search(arr,target))
