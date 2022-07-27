def merge_sort(list):

    # 1. Store the length of the list
    list_length = len(list)

    # 2. Base case: if list is already sorted
    if list_length <= 1:
        return list

    # 3. Identify the list midpoint to partition into left and right
    mid_point = list_length // 2

    # 4. Break the list into left and right, and merge sort each
    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    # 5. Merge!!! (left and right list)
    return merge(left_partition, right_partition)

def merge(left_partition, right_partition):

    # Initialize an output array
    output = []

    # Initialize array points
    i = j = 0

    # initialize length
    left_length = len(left_partition)
    right_length = len(right_partition)

    # Append the smaller elements in both arrays into output (in ascending order)
    while i < left_length and j < right_length:
        if left_partition[i] <= right_partition[j]:
            output.append(left_partition[i])
            i += 1
        else:
            output.append(right_partition[j])
            j += 1

    # Append the remaining elements of left and right
    output.extend(left_partition[i:])
    output.extend(right_partition[j:])

    return output

def run_merge_sort():
    unsorted_list = [4, 7, 9, 0, 0, 1, -1, 20, 100]
    print(unsorted_list)
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)


print(merge([1, 3, 4, 5],[2, 6, 7, 8]))
