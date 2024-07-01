import sys


def max_prod(arr):
    n = len(arr)
    maxi = -sys.maxsize - 1
    for i in range(n):
        for j in range(i,n):
            print(arr[i:j+1])
            s = 1
            for k in range(i,j+1):
                s *= arr[k]
            print(s)
            maxi = max(maxi,s)
    print(f"MAX={maxi}")


def max_prod1(arr):
    n = len(arr)
    maxi = -sys.maxsize - 1
    for i in range(n):
        s = 1
        for j in range(i,n):
            s *= arr[j]
            maxi = max(maxi,s)
    print(f"MAX={maxi}")

def max_prod2(arr):
    n = len(arr)
    pre = 1
    suff = 1
    maxi = -sys.maxsize - 1
    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1
        pre = pre * arr[i]
        suff = suff * arr[n-i-1]
        maxi = max(maxi,max(pre,suff))
    print(f"MAX={maxi}")


arr = [1,2,3,4,5,0]
# arr = [1,2,-3,0,-4,-5]
# max_prod(arr)
# max_prod1(arr)
max_prod2(arr)
