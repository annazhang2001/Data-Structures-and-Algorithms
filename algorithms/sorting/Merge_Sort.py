def quick_sort(list):

    list_length = len(list)

    # Base case: directly return list if there are fewer than 2 elts in list
    if list_length < 2:
        return list

    # Let the pivot be the first element in the array
    pivot_pos = 0

    # Initialize tracker
    tracker = 0

    # Create two buckets
    for i in range(1, list_length):
        if list[pivot_pos] >= list[i]:
            # Increment position tracker
            # Swap
            tracker += 1
            temp = list[tracker]
            list[tracker] = list[i]
            list[i] = temp

    # Swap pivot and tracker
    temp2 = list[pivot_pos]
    list[pivot_pos] = list[tracker]
    list[tracker] = temp2

    # Omit tracker
    left = quick_sort(list[0:tracker])
    right = quick_sort(list[tracker+1:list_length])

    return left + [list[tracker]] + right

def run_quick_sort():
    unsorted_list = [4, 6, 7, 0, 1]
    print(unsorted_list)
    sorted_list = quick_sort(unsorted_list)
    print(sorted_list)

run_quick_sort()
