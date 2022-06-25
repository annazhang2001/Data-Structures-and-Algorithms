class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = [0] * len(nums)
        prefix = 1
        postfix = 1
        
        # Prefix
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # Postfix
        j = len(nums) - 1
        while j >= 0:
            res[j] *= postfix
            postfix *= nums[j]
            j -= 1
        
        return res