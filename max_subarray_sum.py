import sys


def fun(arr):
    n = len(arr)
    maxi = -sys.maxsize - 1
    s = 0
    for i in range(n):
        s += arr[i]

        if s > maxi:
            maxi = s

        if s < 0:
            s = 0
    return s

arr = [1, 2, 3, -2, 5]
print(fun(arr))
