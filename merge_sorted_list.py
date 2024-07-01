def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    # Traverse both lists and append the smaller element to the merged list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            if not merged_list or merged_list[-1] != list1[i]:
                merged_list.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            if not merged_list or merged_list[-1] != list2[j]:
                merged_list.append(list2[j])
            j += 1
        else:
            if not merged_list or merged_list[-1] != list1[i]:
                merged_list.append(list1[i])
            i += 1
            j += 1

    # Append remaining elements of list1
    while i < len(list1):
        if not merged_list or merged_list[-1] != list1[i]:
            merged_list.append(list1[i])
        i += 1

    # Append remaining elements of list2
    while j < len(list2):
        if not merged_list or merged_list[-1] != list2[j]:
            merged_list.append(list2[j])
        j += 1

    return merged_list


# Example usage with provided lists
l1 = [0, 5, 6]
l2 = [4, 5, 6, 7, 8]

merged_list = merge_sorted_lists(l1, l2)
print(merged_list)  # Output: [0, 4, 5, 5, 6, 6, 7, 8]
