def merge(left, right):
    res = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])
    return res


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    l_half = arr[:mid]
    r_half = arr[mid:]
    l_half = merge_sort(l_half)
    r_half = merge_sort(r_half)
    return merge(l_half, r_half)

arr = [3,1,2,6,4,9,0]
print(merge_sort(arr))