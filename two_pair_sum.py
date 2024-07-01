#Two Sum : Check if a pair with given sum exists in Array
"""
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
Result: YES (for 1st variant)
       [1, 3] (for 2nd variant)
Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

Example 2:
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 15
Result: NO (for 1st variant)
	[-1, -1] (for 2nd variant)
Explanation: There exist no such two numbers whose sum is equal to the target.
"""

arr = [2,6,5,8,11]
target = 14
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print("YES")
            print(arr[i], arr[j])
            print(i,j)
        else:
            continue

print(arr)
arr = sorted(arr)
print(arr)
left = 0
right = len(arr) - 1
while left<right:
    sum = arr[left] + arr[right]
    if sum == target:
        print("YES")
        break
    elif sum < target:
        left += 1
    else:
        right -= 1
else:
    print("NO")

