class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        totalSum = 0
        for n in nums:
            totalSum += n
        
        curSum = 0
        for i in range(len(nums)):
            if curSum == totalSum - curSum - nums[i]:
                return i

            curSum += nums[i]
        
        
        return -1