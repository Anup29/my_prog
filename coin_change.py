def countWaysToMakeChangeUntil(arr, ind, T, dp):
    if ind == 0:
        return 1 if T % arr[0] == 0 else 0
    if dp[ind][T] != -1:
        return dp[ind][T]

    not_taken = countWaysToMakeChangeUntil(arr, ind-1, T, dp)

    taken = 0
    if arr[ind] <= T:
        taken = countWaysToMakeChangeUntil(arr, ind, T-arr[ind], dp)

    dp[ind][T] = not_taken + taken
    return dp[ind][T]
def countWaysToMakeChange(arr, n, T):
    dp = [[-1 for i in range(T+1)] for j in range(n)]
    return countWaysToMakeChangeUntil(arr, n-1, T, dp)

def main():
    arr = [1,2,3]
    target = 4
    n = len(arr)
    print(f"Total no of ways:{countWaysToMakeChange(arr,n,target)}")

if __name__ == "__main__":
    main()