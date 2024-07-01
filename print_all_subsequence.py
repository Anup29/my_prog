def fun(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            print(arr[i:j+1])


arr = "aa"
fun(arr)