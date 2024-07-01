def fun(i,j,n,m,dp):
    if i == n-1 and j == m-1:
        return 1
    if i >=n or j >=m:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    else:
        dp[i][j] = fun(i+1,j,n,m,dp)+fun(i,j+1,n,m,dp)
        return dp[i][j]

def uniqPath(n,m):
    dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
    num = fun(0,0,n,m,dp)
    if m ==1 and n== 1:
        return num
    return dp[0][0]

tot = uniqPath(3,7)
print(tot)