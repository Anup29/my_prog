def combinationSum(arr, target):
    ans =[]
    ds= []
    def fun(ind, target):
        if ind == len(arr):
            if target == 0:
                ans.append(ds[:])
            return
        if arr[ind] <= target:
            ds.append(arr[ind])
            fun(ind, target-arr[ind])
            ds.pop()
        fun(ind+1, target)
    fun(0, target)
    return ans

if __name__ == "__main__":
    candidates = [2, 3, 6, 7, 4]
    target = 7
    ans = combinationSum(candidates, target)
    print("Combinations are: ")
    for combination in ans:
        print(" ".join(map(str, combination)))
