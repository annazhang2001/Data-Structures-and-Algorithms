def Insertion_Sort(nums):
    # Insertion Sort
        
    for i in range(1, len(nums)):   
        value_to_sort = nums[i]
            
        j = i
        while j > 0 and value_to_sort < nums[j-1]:
            # Swap
            tmp = nums[j-1]
            nums[j-1] = value_to_sort
            nums[j] = tmp
            j -= 1
            
        
    return nums