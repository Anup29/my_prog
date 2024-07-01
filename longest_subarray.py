def longestSubarray(arr, k):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i,n):
            print(arr[i:j+1])
            s = 1
            for p in range(i,j+1):
                s *= arr[p]
            print(s)
            if s <= k:
                count += 1
    print(f"COUNT:{count}")


def longestSubarray1(arr,k):
    n = len(arr)
    count = 0
    for i in range(n):
        s=1
        for j in range(i,n):
            s *= a[j]
        if s<= k:
            count += 1
    print(f"Count: {count}")

if __name__ == "__main__":
    a = [1, 2, 3]
    k = 4
    length = 0
    length = longestSubarray(a, k)
    length = longestSubarray1(a, k)

    print(f"The length of the longest subarray is: {length}")
