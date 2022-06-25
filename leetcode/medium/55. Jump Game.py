class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        
        farthest = 0
        
        for i in range(n-1):
            farthest = farthest if (farthest > nums[i] + i) else nums[i] + i
            
            # Encountered zero
            if farthest <= i:
                return False
        
    
        return farthest >= (n-1)