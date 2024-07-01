import sys


def max_sub_sum(arr):
    n = len(arr)
    maxi = arr[0]
    for i in range(n):
        for j in range(i,n):
            print(arr[i:j+1])
            s = 0
            for k in range(i,j+1):
                s += arr[k]
            print(s)
            maxi = max(maxi,s)
    print(maxi)

def max_sub_sum1(arr):
    n = len(arr)
    maxi = -sys.maxsize - 1
    for i in range(n):
        s = 0
        for j in range(i,n):
            s += arr[j]
            maxi = max(maxi, s)
    print(maxi)

def max_sub_sum2(arr):
    n = len(arr)
    maxi = -sys.maxsize - 1
    s = 0
    for i in range(n):
        s += arr[i]
        if s > maxi:
            maxi = s
        if s < 0:
            s = 0
    print(maxi)

def max_sub_sum3(arr):
    n = len(arr)
    s = 0
    maxi = -sys.maxsize - 1
    start = 0
    startIndex = -1
    endIndex = -1
    for i in range(n):
        if(s == 0):
            start = i
        s += arr[i]

        if s > maxi:
            maxi = s
            startIndex = start
            endIndex = i
        if s < 0:
            s = 0
    print(f"MAX SUM={maxi}")
    print("Sub Array :")
    for i in range(startIndex,endIndex+1):
        print(arr[i], end= " ")


# arr = [1,2,3,4]
arr = [-2,1,-3,4,-1,2,1,-5,4]
# arr = [1]
# max_sub_sum(arr)
# max_sub_sum1(arr)
# max_sub_sum2(arr)
max_sub_sum3(arr)