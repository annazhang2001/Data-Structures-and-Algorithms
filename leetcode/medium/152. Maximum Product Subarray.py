class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = max(nums)
        curMax = 1
        curMin = 1
        
        for n in nums:

                
            tmp = curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * tmp, n * curMin, n)
            
            res = max(res, curMax)
            
        return res