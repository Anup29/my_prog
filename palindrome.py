def fun(i,arr):
    n = len(arr)
    if i>=n//2:
        return True
    if arr[i] != arr[n-i-1]:
        return False
    return fun(i+1, arr)

arr = "madam"
print(fun(0,arr))
