#Kadane's Algorithm : Maximum Subarray Sum in an Array
"""
Example 1:
Input:
 arr = [-2,1,-3,4,-1,2,1,-5,4]

Output:
 6

Explanation:
 [4,-1,2,1] has the largest sum = 6.

Examples 2:
Input:
 arr = [1]

Output:
 1
"""

import sys
def fun(arr):
    n = len(arr)
    s = 0
    start = 0
    startIndex = -1
    endIndex = -1
    maxi = - sys.maxsize - 1
    for i in range(n):
        if s == 0 :
            start = i
        s += arr[i]
        if s > maxi:
            maxi = s
            startIndex = start
            endIndex = i
        if s < 0:
            s = 0
    for i in range(startIndex,endIndex+1):
        print(arr[i])
    print(f"Sum={maxi}")


arr = [-2,1,-3,4,-1,2,1,-5,4]
fun(arr)
# n = len(arr)
# maxi = -sys.maxsize - 1
# for i in range(n):
#     for j in range(i,n):
#         summ = 0
#         for k in range(i,j+1):
#             summ += arr[k]
#
#         maxi = max(maxi, summ)
#
# print(maxi)

