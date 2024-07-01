def find_subarrays(arr):
    subarrays = []
    n = len(arr)
    for start in range(n):
        for end in range(start + 1, n + 1):
            subarrays.append(arr[start:end])
    return subarrays

# Example usage
array = [1, 2, 3]
subarrays = find_subarrays(array)
print(subarrays)
