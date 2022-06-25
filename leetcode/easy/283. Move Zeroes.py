class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return []
            
        # Fast slow pointer
        slow = 0
        fast = 0
        
        while fast < n:
            
            if nums[fast] != 0:
                tmp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = tmp
                slow += 1
            
            fast += 1
        