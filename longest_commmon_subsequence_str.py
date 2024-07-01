def lcs(s1,s2):
    n, m = len(s1), len(s2)
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    return lcsUtils(s1, s2, n-1, m-1, dp)

def lcsUtils(s1,s2,ind1, ind2,dp):
    if ind1<0 or ind2 <0:
        return 0
    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]
    if s1[ind1] == s2[ind2]:
        dp[ind1][ind2] = 1 + lcsUtils(s1,s2,ind1-1,ind2-1,dp)
    else:
        dp[ind1][ind2]= 0 + max(lcsUtils(s1,s2, ind1-1,ind2,dp), lcsUtils(s1,s2,ind1,ind2-1,dp))
    return dp[ind1][ind2]


#Tabulation
def lcs_tab(s1,s2):
    n,m = len(s1), len(s2)
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 0
    for j in range(m+1):
        dp[0][j] = 0

    for ind1 in range(1,n+1):
        for ind2 in range(1,m+1):
            if s1[ind1-1] == s2[ind2-1]:
                dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
            else:
                dp[ind1][ind2] = 0 + max((dp[ind1-1][ind2], dp[ind1][ind2-1]))
    return dp[n][m]

def main():
    s1 = "acdgh"
    s2 = "cedgh"
    print(lcs(s1,s2))
    print(lcs_tab(s1,s2))
#
# if __name__ == "__main__":
#     main()
#

def lcs(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for j in range(m+1):
        dp[0][j] = 0
    for ind1 in range(1,n+1):
        for ind2 in range(1,m+1):
            if s1[ind1-1] == s2[ind2-1]:
                dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
            else:
                dp[ind1][ind2] = 0 + max(dp[ind1-1][ind2], dp[ind1][ind2-1])
    return dp[n][m]


s1 = "acd"
s2 = "ced"
print(lcs(s1,s2))