def main():
    n =6
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1
    print(dp[0])
    print(dp[1])

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
        print(dp[i])

    print(dp[n])

def main1():
    n = 5
    prev2 = 0
    prev = 1

    for i in range(2,n+1):
        curi = prev2 + prev
        prev2 = prev
        prev = curi
    print(prev)


if __name__ == '__main__':
    main()
    main1()
