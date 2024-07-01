from typing import *

def search(arr: List[int], target: int) -> bool:
    n = len(arr)
    low, high = 0, n-1
    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == target:
            return True

        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low = low+1
            high = high-1
            continue

        if arr[low] <= arr[mid]:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return False


arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
target = 3
print(search(arr,target))