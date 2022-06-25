class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Initialize hash map
        remainders = {0: -1}
        curSum = 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            remainder = curSum % k
            
            if remainder in remainders:
                if (i - remainders[remainder]) >= 2:
                    return True
            else:
                remainders[remainder] = i
        
        return False
        