class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            j = i-1
            while j >= 0:
                if nums[i] > nums[j]:
                    dp[i] = dp[i] if dp[i] >= (dp[j]+1) else (dp[j]+1)
                j -= 1
            
        
        max = 0
        for i in range(len(dp)):
            if dp[i] > max:
                max = dp[i]
        
        return max