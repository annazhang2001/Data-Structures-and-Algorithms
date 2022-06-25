class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # not in place
        length = len(nums)
        new_lst = length * [0]
    
        k = k % length
        
        new_lst[0: k] = nums[length-k: length]
        new_lst[k: length] = nums[0: length-k]
        
        for i in range(length):
            nums[i] = new_lst[i]
            
        return nums