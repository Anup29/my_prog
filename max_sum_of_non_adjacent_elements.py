"""
N=3
arr = [1,2,4]
output: 5
N=4
arr=[2,1,4,9]
output: 11(2+9)
"""
#Memoization
def fun(ind, arr, dp):
    if ind == 0:
        return arr[ind]
    if ind < 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]

    pick = arr[ind] + fun(ind-2,arr,dp)
    notPick = 0 + fun(ind-1,arr,dp)
    dp[ind] = max(notPick,pick)
    return dp[ind]

#Tabulization
def tabu(n,arr,dp):
    dp[0] = arr[0]
    for i in range(1,n):
        pick = arr[i]
        if i>1:
            pick = pick + dp[i-2]
        non_pic = 0 + dp[i-1]
        dp[i] = max(pick,non_pic)
    return dp[-1]

#Space optimized
def space_opti(n, arr):
    prev = arr[0]
    prev2 = 0
    for i in range(1,n):
        pick = arr[i]
        if i > 1:
            pick = pick + prev2
        no_pick = 0 + prev
        curi = max(pick, no_pick)
        prev2 = prev
        prev = curi
    return prev

def main():
    arr = [1,5,9,11]
    n = len(arr)
    dp = [-1 for _ in range(n)]
    # res = fun(n-1,arr,dp)
    # print(res)
    res = tabu(n,arr,dp)
    print(res)
    res = space_opti(n, arr)
    print(res)

if __name__ == "__main__":
    main()
