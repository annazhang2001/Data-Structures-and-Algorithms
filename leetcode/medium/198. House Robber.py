class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Optimized dp
        dp_1 = 0
        dp_2 = 0
        
        for i in range(n-1, -1, -1):
            dp_i = max(nums[i]+dp_2, dp_1)
            
            dp_2 = dp_1
            dp_1 = dp_i
        
        return dp_1
        
        