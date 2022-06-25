class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
https://leetcode.com/problems/subarray-sum-equals-k/solution/        :type k: int
        :rtype: int
        """
        
        prefixSum = 0
        count = 0
        maps = {0: 1}
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            
            if prefixSum - k in maps:
                count += maps[prefixSum-k]
            
            maps[prefixSum] = maps.get(prefixSum, 0) + 1
            
        return count