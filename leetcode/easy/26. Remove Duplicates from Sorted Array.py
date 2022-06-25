class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        # initialize slow and fast pointers
        slow = 0
        fast = 0
        
        while fast < n:
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        
        return slow+1
        
        
        
        