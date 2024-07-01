from typing import *

def find_missing(arr: [int])-> int :
    n = len(arr)
    ele = 0
    for i in range(n):
        if i+1 in arr:
            continue
        else:
            ele = i+1
            break
    return ele


def find_missing1(arr: [int])-> int :
    n = len(arr)
    hash = [0] * (n+1)

    for i in range(n-1):
        hash[arr[i]] += 1

    for i in range(1,n+1):
        if hash[i] == 0:
            return i

def find_missing2(arr: [int])-> int :
    n = len(arr) + 1
    s1 = n * (n+1) // 2
    s2 = sum(arr)
    ans = s1 - s2
    return ans


def find_missing3(arr: [int])-> int :
    n = len(arr)
    xor1 = 0
    xor2 = 0
    for i in range(n-1):
        xor1 = xor1 ^ arr[i]
        xor2 = xor2 ^ i+1

    xor2 = xor2 ^ n

    res = xor1 ^ xor2
    return res

arr = [1,2,4,5]
print(find_missing(arr))
print(find_missing1(arr))
print(find_missing2(arr))
print(find_missing3(arr))
