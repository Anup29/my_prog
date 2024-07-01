import sys
from typing import *
def search(arr: [int]):
    n = len(arr)
    low, high = 0, n-1
    ans = sys.maxsize
    while low <= high:
        mid = (low+high) // 2
        if arr[low] <= arr[high]:
            ans = min(ans, arr[low])
            break
        if arr[low] <= arr[mid]:
            ans = min(ans,arr[low])
            low = mid + 1
        else:
            ans = min(ans,arr[mid])
            high = mid - 1
    return  ans

arr = [4, 5, 6, 7, 2, 3]

ans = search(arr)
print("The minimum element is:", ans)