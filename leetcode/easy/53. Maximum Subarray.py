class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        max_sum = nums[0]
        
        # Base case:
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        for i in range(len(dp)):
            if max_sum < dp[i]:
                max_sum = dp[i]
                
        return max_sum