"""
Sample Input 2:
3
5
1 5 1 2 6
3
2 3 5
4
1 3 2 0
Sample Output 2:
11
5
3
"""
def fun(n, arr):
    prev= arr[0]
    prev2 = 0
    for i in range(1,n):
        take = arr[i]
        if i > 1:
            take = take + prev2
        no_take = 0 + prev
        curi = max(take, no_take)
        prev2 = prev
        prev = curi
    return prev

arr = [2,1,4,9]
arr = [1,5,2,1,6]
n = len(arr)
tmp1 = arr[1:]
tmp2 = arr[:n-2]
res = max(fun(len(tmp1),tmp1), fun(len(tmp2), tmp2))
# print(fun(n, arr))
print(res)