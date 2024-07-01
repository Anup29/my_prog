#Contains Duplicate : Check if a value appears atleast twice
"""
Example 1:
Input: nums = [1, 2, 3, 1]
Output: true.
Explanation: 1 appeared two times in the input array.

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
Explanation: input array does not contain any duplicate number.
"""

# nums = [1, 2, 3, 1]
nums = [1, 2, 3, 4]
for i in range(len(nums)):
    if nums[i] in nums[i+1:]:
        print("true")
else:
    print("false")