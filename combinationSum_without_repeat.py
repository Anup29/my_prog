def combSum(arr, target):
    ans = []
    ds = []
    arr.sort()
    def fun(ind, target):
        if target == 0:
            ans.append(ds[:])
            return
        for i in range(ind, len(arr)):
            if i> ind and arr[i] == arr[i-1]:
                continue
            if arr[i] > target:
                break
            ds.append(arr[i])
            fun(ind+1, target-arr[i])
            ds.pop()
    fun(0, target)
    return ans



arr = [10,2,7,6,1,5]
s = combSum(arr, 8)
print(s)